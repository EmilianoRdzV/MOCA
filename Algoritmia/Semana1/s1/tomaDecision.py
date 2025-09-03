def ejecutarDiagramaDeFlujo():
    try:
        a, b = map(int, input().split())
    except (ValueError, IndexError):
        return

    resultado = 0
    if (a + b) == 5:
        b += 3
        resultado = 2 * a + b
    else:
        a -= 1
        if (7 * a + b) % 2 == 0:
            resultado = a - b
        else:
            resultado = a * b

    print(resultado)

if __name__ == "__main__":
    ejecutarDiagramaDeFlujo()