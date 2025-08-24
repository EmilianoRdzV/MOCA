def sumarNNumeros():
    try:
        n = int(input())
    except (ValueError, IndexError):
        return

    sumaTotal = 0
    for _ in range(n):
        numero = int(input())
        sumaTotal += numero

    print(sumaTotal)

if __name__ == "__main__":
    sumarNNumeros()