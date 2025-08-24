def realizarOperaciones():
    try:
        a, b = map(int, input().split())
    except (ValueError, IndexError):
        return

    suma = a + b
    resta = a - b
    divisionEntera = a // b
    multiplicacion = a * b
    modulo = a % b

    resultados = [suma, resta, divisionEntera, multiplicacion, modulo]

    print(" ".join(map(str, resultados)))

if __name__ == "__main__":
    realizarOperaciones()