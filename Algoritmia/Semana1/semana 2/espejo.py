try:
    m, n = map(int, input().split())

    for _ in range(m):
        fila = input().split()
        fila_invertida = fila[::-1]
        print(" ".join(fila_invertida))

except Exception as e:
    print("Error:", e)
