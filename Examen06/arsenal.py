import sys

# Leer N
n = int(sys.stdin.readline())

# Leer los N poderes en una lista
poderes = list(map(int, sys.stdin.readline().split()))

# Encontrar el poder máximo
maxPoder = max(poderes)

# Encontrar el índice 0-basado del poder máximo
# .index() encuentra la *primera* aparición
idxCero = poderes.index(maxPoder)

# Convertir el índice a 1-basado
idxUno = idxCero + 1

# Imprimir sin salto de línea al final
print(f"{maxPoder} {idxUno}", end="")