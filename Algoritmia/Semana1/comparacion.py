def clasificarNumero():
    try:
        numero = int(input())
    except (ValueError, IndexError):
        return

    if numero > 0:
        print("POSITIVO")
    elif numero < 0:
        print("NEGATIVO")
    else:
        print("CERO")

if __name__ == "__main__":
    clasificarNumero()