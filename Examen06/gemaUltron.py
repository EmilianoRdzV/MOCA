import sys

# Leer N
n = int(sys.stdin.readline())

# Leer los N dulces en una lista
dulces = list(map(int, sys.stdin.readline().split()))

# Leer K
k = int(sys.stdin.readline())

gemas = []

# Iteramos sobre los dulces en su orden original
for d in dulces:
    cond1 = (d >= k and d <= k + 3)
    cond2 = (d >= k - 3 and d < k)
    
    if cond1 or cond2:
        # Añadimos el número como string para unirlo después
        gemas.append(str(d))

# Imprimimos la lista unida por espacios, sin salto de línea al final
print(" ".join(gemas), end="")