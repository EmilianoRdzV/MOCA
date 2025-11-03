import sys

n = int(sys.stdin.readline())
                    
mat1 = []
mat2 = []

for i in range(n):
    fila = []
    for j in range(n):
        num = int(sys.stdin.readline())
        fila.append(num)
    mat1.append(fila)

for i in range(n):
    fila = []
    for j in range(n):
        num = int(sys.stdin.readline())
        fila.append(num)
    mat2.append(fila)

for i in range(n):
    fila_salida = []
    for j in range(n):
        suma = mat1[i][j] + mat2[i][j]
        fila_salida.append(str(suma))
    print(" ".join(fila_salida))
