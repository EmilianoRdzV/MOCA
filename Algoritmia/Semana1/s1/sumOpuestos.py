n = int(input())
listaNumeros = list(map(int, input().split()))

listaSumas = []
numeroDePares = n // 2

for i in range(numeroDePares):
    suma = listaNumeros[i] + listaNumeros[n - 1 - i]
    listaSumas.append(suma)

print(*listaSumas)