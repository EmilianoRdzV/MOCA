numeros = list(map(int, input().split()))
numeros.sort()

a = numeros[0]
b = numeros[1]
c = numeros[2]

if a**2 + b**2 == c**2:
    print("SI")
else:
    print("NO")