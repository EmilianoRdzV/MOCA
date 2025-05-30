def imprimir_rectangulo_asteriscos():
    """
    Lee dos enteros N y M, e imprime un rectángulo de N x M asteriscos.
    """
    # Lee los dos enteros N y M de la misma línea, separados por un espacio.
    # input().split() divide la cadena de entrada por espacios, devolviendo una lista de cadenas.
    # map(int, ...) aplica la función int a cada elemento de esa lista.
    try:
        n, m = map(int, input().split())
    except ValueError:
        # Manejo básico de error si la entrada no son dos números.
        # Para OmegaUp, usualmente se asume que la entrada es correcta.
        print("Entrada inválida. Por favor ingrese dos números enteros separados por espacio.")
        return

    # Validar que N y M estén dentro de los límites especificados (1 a 100).
    # Aunque en OmegaUp generalmente se asume que la entrada cumple los límites,
    # es buena práctica considerarlos.
    if not (1 <= n <= 100 and 1 <= m <= 100):
        # En un entorno competitivo, este tipo de validación explícita
        # podría no ser necesaria si se garantiza que la entrada siempre es válida.
        # Si se imprime un mensaje de error, podría considerarse una salida incorrecta.
        # Para este caso, procederemos asumiendo que los límites se cumplen si no se especifica lo contrario.
        pass # Se asume que la entrada de OmegaUp será válida.


    # Iterar N veces para cada renglón
    for _ in range(n):
        # En cada renglón, imprimir M asteriscos.
        # La expresión '*' * m crea una cadena con 'm' asteriscos.
        # print() por defecto añade un salto de línea al final.
        print('*' * m)

if __name__ == "__main__":
    imprimir_rectangulo_asteriscos()