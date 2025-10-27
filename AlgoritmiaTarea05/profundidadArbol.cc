#include <iostream>
#include <vector>
#include <queue>
#include <algorithm> // Para std::min y std::max
#include <climits>   // Para INT_MAX

// 1. Definimos un struct Nodo adaptado al problema
struct Nodo {
    int columna;
    struct Nodo* izq;
    struct Nodo* der;
    
    // Constructor para inicializar los valores
    Nodo() : columna(0), izq(NULL), der(NULL) {}
};

// Arreglo global para guardar todos los nodos (1-indexado)
Nodo nodos[1001];
// Contador global para asignar columnas
int colGlobal = 1;

/**
 * 2. Recorrido In-Orden (DFS) para asignar las columnas
 * Izquierda -> Raíz -> Derecha
 */
void asignarColumnas(Nodo* nodo) {
    if (nodo == NULL) {
        return;
    }
    // 1. Vamos a la izquierda
    asignarColumnas(nodo->izq);
    
    // 2. Visitamos la raíz (le asignamos columna)
    nodo->columna = colGlobal++;
    
    // 3. Vamos a la derecha
    asignarColumnas(nodo->der);
}

int main() {
    int n;
    std::cin >> n;

    // --- PASO 1: Construir el Árbol ---
    for (int i = 0; i < n; ++i) {
        int id, idIzq, idDer;
        std::cin >> id >> idIzq >> idDer;
        
        // Asignamos los punteros de hijos
        if (idIzq != -1) {
            nodos[id].izq = &nodos[idIzq];
        }
        if (idDer != -1) {
            nodos[id].der = &nodos[idDer];
        }
    }

    // --- PASO 2: Asignar Columnas ---
    // Empezamos desde la raíz, que siempre es el nodo 1
    asignarColumnas(&nodos[1]);

    // --- PASO 3: Calcular Anchos por Nivel (BFS) ---
    // Vectores para guardar el min/max de cada nivel
    std::vector<int> minColPorNivel(n + 1, INT_MAX);
    std::vector<int> maxColPorNivel(n + 1, 0);

    // Cola para el BFS: guarda {Puntero al Nodo, Nivel}
    std::queue<std::pair<Nodo*, int>> q; 
    
    // Empezamos en la raíz (Nodo 1) en el Nivel 1
    q.push({&nodos[1], 1});
    minColPorNivel[1] = nodos[1].columna;
    maxColPorNivel[1] = nodos[1].columna;
    int maxNivelAlcanzado = 1;

    while (!q.empty()) {
        std::pair<Nodo*, int> actual = q.front();
        q.pop();
        
        Nodo* nodo = actual.first;
        int nivel = actual.second;
        
        maxNivelAlcanzado = std::max(maxNivelAlcanzado, nivel);
        int nivelHijo = nivel + 1;

        // Procesar hijo izquierdo
        if (nodo->izq != NULL) {
            q.push({nodo->izq, nivelHijo});
            // Actualizar min/max para el nivel del hijo
            minColPorNivel[nivelHijo] = std::min(minColPorNivel[nivelHijo], nodo->izq->columna);
            maxColPorNivel[nivelHijo] = std::max(maxColPorNivel[nivelHijo], nodo->izq->columna);
        }
        
        // Procesar hijo derecho
        if (nodo->der != NULL) {
            q.push({nodo->der, nivelHijo});
            // Actualizar min/max para el nivel del hijo
            minColPorNivel[nivelHijo] = std::min(minColPorNivel[nivelHijo], nodo->der->columna);
            maxColPorNivel[nivelHijo] = std::max(maxColPorNivel[nivelHijo], nodo->der->columna);
        }
    }

    // --- PASO 4: Encontrar el Ancho Máximo ---
    int maxAncho = 0;
    int nivelMaxAncho = 0;

    for (int i = 1; i <= maxNivelAlcanzado; ++i) {
        // Ancho = col_max - col_min + 1
        int anchoActual = maxColPorNivel[i] - minColPorNivel[i] + 1;
        
        // La regla es: si es MÁS GRANDE, se actualiza.
        // Si es igual, se queda el nivel anterior (más pequeño).
        if (anchoActual > maxAncho) {
            maxAncho = anchoActual;
            nivelMaxAncho = i;
        }
    }

    // --- Salida ---
    std::cout << nivelMaxAncho << " " << maxAncho << std::endl;

    return 0;
}