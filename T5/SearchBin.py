def SearchBin():
    # Leer N
    n = int(input())

    # Leer la secuencia A y almacenarla en un conjunto para búsquedas eficientes
    set_a = set()
    if n > 0:
        # Leer los N enteros de la secuencia A, que están en una sola línea separados por espacios
        a_elements = list(map(int, input().split()))
        set_a = set(a_elements)
    # Si n es 0, set_a permanece como un conjunto vacío, y no se intenta leer una línea para A.

    # Leer M
    m = int(input())

    # Leer la secuencia B
    list_b = []
    if m > 0:
        # Leer los M enteros de la secuencia B
        list_b = list(map(int, input().split()))
    # Si m es 0, list_b permanece como una lista vacía.

    results = []
    # Para cada elemento en B, verificar si está en A
    for b_element in list_b:
        if b_element in set_a:
            results.append("1")
        else:
            results.append("0")

    # Imprimir los resultados en una sola línea, separados por espacios
    # Si results está vacío (porque M=0), " ".join([]) produce una cadena vacía,
    # y print() imprimirá solo un salto de línea, lo cual es un comportamiento estándar.
    print(" ".join(results))

if __name__ == "__main__":
    SearchBin()