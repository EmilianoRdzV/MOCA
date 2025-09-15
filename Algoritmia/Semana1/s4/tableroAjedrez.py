letra, fila = input().split()
col = ord(letra.lower()) - ord('a') + 1
fila = int(fila)

if (col + fila) % 2 == 0:
    print("NEGRO")
else:
    print("BLANCO")