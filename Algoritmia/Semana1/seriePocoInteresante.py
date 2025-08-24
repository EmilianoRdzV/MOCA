def calcularSerie():
    try:
        n, p = map(int, input().split())
    except (ValueError, IndexError):
        return

    numeroAntes = ((n - 1 - p) % 3) + 1
    numeroDespues = ((n - 1 + p) % 3) + 1

    print(numeroAntes, numeroDespues)

if __name__ == "__main__":
    calcularSerie()