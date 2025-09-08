#include <stdio.h>
#include <stdlib.h>

int main() {
    int frecuencia;
    scanf("%d", &frecuencia);

    if (frecuencia < 540 || frecuencia > 1520) {
        printf("error\n");
        return 0;
    }

    int estaciones[] = {580, 980, 1190, 1250, 1420};
    int n = sizeof(estaciones) / sizeof(estaciones[0]);

    int distanciaMinima = abs(frecuencia - estaciones[0]);
    int estacionMasCercana = estaciones[0];
    int posicion = 0;

    for (int i = 1; i < n; i++) {
        int distanciaActual = abs(frecuencia - estaciones[i]);
        if (distanciaActual < distanciaMinima) {
            distanciaMinima = distanciaActual;
            estacionMasCercana = estaciones[i];
            posicion = i;
        } else if (distanciaActual == distanciaMinima && estaciones[i] > frecuencia) {
            estacionMasCercana = estaciones[i];
            posicion = i;
        }
    }

    int diferencia = estacionMasCercana - frecuencia;

    if (diferencia == 0) {
        printf("adelante 0\n");
    } else if (diferencia > 0) {
        printf("adelante %d\n", diferencia);
    } else {
        printf("atras %d\n", -diferencia);
    }

    return 0;
}
