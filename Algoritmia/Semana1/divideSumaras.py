def dividirYSumar():
    try:
        n = int(input())
    except (ValueError, IndexError):
        return

    sumaTotal = 0
    while n > 0:
        sumaTotal += n
        n //= 2

    print(sumaTotal)

if __name__ == "__main__":
    dividirYSumar()