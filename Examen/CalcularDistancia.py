import math

def CalcularDistancia(x1, y1, x2, y2):
    """
    Calcula la distancia euclidiana entre dos puntos (x1,y1) y (x2,y2).
    """
    delta_x = x2 - x1
    delta_y = y2 - y1
    # Distancia = sqrt(delta_x^2 + delta_y^2)
    return math.sqrt(delta_x**2 + delta_y**2)

def EncontrarLadoMasCortoDelCuadrilatero():
    """
    Lee las coordenadas de los 4 vértices de un cuadrilátero,
    calcula la longitud de cada lado, y luego imprime la longitud del lado más corto.
    """
    try:
        puntos = []
        # Leer las coordenadas de los 4 vértices.
        # El problema indica "Ocho reales" y el ejemplo muestra 4 líneas,
        # cada una con un par de coordenadas (x, y).
        for _ in range(4):
            # map(float, ...) convierte las entradas separadas por espacio a números flotantes
            x, y = map(float, input().split())
            puntos.append((x, y))

        # Los puntos son:
        # p0 = puntos[0] = (x1, y1)
        # p1 = puntos[1] = (x2, y2)
        # p2 = puntos[2] = (x3, y3)
        # p3 = puntos[3] = (x4, y4)
        # Se listan en el sentido de las manecillas del reloj.

        # Calcular la longitud de los 4 lados del cuadrilátero:
        # Lado 1: entre el punto 0 (x1,y1) y el punto 1 (x2,y2)
        longitud_lado1 = CalcularDistancia(puntos[0][0], puntos[0][1], puntos[1][0], puntos[1][1])
        
        # Lado 2: entre el punto 1 (x2,y2) y el punto 2 (x3,y3)
        longitud_lado2 = CalcularDistancia(puntos[1][0], puntos[1][1], puntos[2][0], puntos[2][1])
        
        # Lado 3: entre el punto 2 (x3,y3) y el punto 3 (x4,y4)
        longitud_lado3 = CalcularDistancia(puntos[2][0], puntos[2][1], puntos[3][0], puntos[3][1])
        
        # Lado 4: entre el punto 3 (x4,y4) y el punto 0 (x1,y1) (para cerrar la figura)
        longitud_lado4 = CalcularDistancia(puntos[3][0], puntos[3][1], puntos[0][0], puntos[0][1])

        # Encontrar la longitud mínima entre los cuatro lados
        lado_mas_corto = min(longitud_lado1, longitud_lado2, longitud_lado3, longitud_lado4)

        # Imprimir el resultado.
        # El problema indica "Un real impreso..." y "razonablemente cercano".
        # El ejemplo de salida tiene 6 decimales. Formatearemos a 7 para seguridad
        # o se podría usar print(lado_mas_corto) para la precisión por defecto de Python.
        print(f"{lado_mas_corto:.7f}") # Imprime con 7 cifras decimales

    except ValueError:
        # Manejo si la entrada no son números flotantes o no hay dos por línea.
        # En OmegaUp, usualmente se asume que la entrada es válida.
        pass
    except Exception as e:
        # Cualquier otro error inesperado.
        pass

if __name__ == "__main__":
    EncontrarLadoMasCortoDelCuadrilatero()