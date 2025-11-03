import sys

# Lee N
n = int(sys.stdin.readline())

# Lee el conjunto A y lo convierte en lista
a = list(map(int, sys.stdin.readline().split()))

# Lee el conjunto B y lo convierte en lista
b = list(map(int, sys.stdin.readline().split()))

# Ordena ambas listas
a.sort()
b.sort()

# Compara las listas (Python puede compararlas directamente)
if a == b:
    print("SI", end="")
else:
    print("NO", end="")