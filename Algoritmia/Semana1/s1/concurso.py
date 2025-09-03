def contarEnLinea():
    try:
        N = int(input())
    except (ValueError, IndexError):
        return

    numeros = list(range(1, N + 1))
    
    print(" ".join(map(str, numeros)))

if __name__ == "__main__":
    contarEnLinea()