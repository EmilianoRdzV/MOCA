def resolver():
    n = int(input())
    matriz = []
    for _ in range(n):
        fila = list(map(int, input().split()))
        matriz.append(fila)

    if n == 0:
        print(1)
        return

    sumaObj = sum(matriz[0])

    
    for i in range(1, n):
        if sum(matriz[i]) != sumaObj:
            print(0)
            return
        
    for j in range(n):
        sumaCol = 0
        for i in range(n):
            sumaCol += matriz[i][j]
        if sumaCol != sumaObj:
            print(0)
            return

    sumaDiag1 = 0
    sumaDiag2 = 0
    for i in range(n):
        sumaDiag1 += matriz[i][i]
        sumaDiag2 += matriz[i][n - 1 - i]

    if sumaDiag1 != sumaObj or sumaDiag2 != sumaObj:
        print(0)
        return

    print(1)

resolver()