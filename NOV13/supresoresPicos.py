
n = int(input())

for _ in range(n):

    linea = list(map(int, input().split()))
    
    k = linea[0]
    outlets = linea[1:]
    sumaOutlets = sum(outlets)

    resultado = sumaOutlets - k + 1
    
    print(resultado)