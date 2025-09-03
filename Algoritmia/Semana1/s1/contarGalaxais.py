def compararGalaxias():
    try:
        a, b, c = map(int, input().split())
    except (ValueError, IndexError):
        return

    resultados = [
        a < b,
        c > a,
        a == b,
        a != c,
        c <= b
    ]

    print(" ".join(map(str, resultados)))

if __name__ == "__main__":
    compararGalaxias()