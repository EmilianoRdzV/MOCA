def contarHastaN():
    try:
        n = int(input())
    except (ValueError, IndexError):
        return

    for i in range(1, n + 1):
        print(i)

if __name__ == "__main__":
    contarHastaN()