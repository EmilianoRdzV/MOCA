n = int(input())
listaNumeros = []

for _ in range(n):
    num = int(input())
    listaNumeros.append(num)

valMin = min(listaNumeros)
valMax = max(listaNumeros)
promedio = sum(listaNumeros) / n
promedioInt = int(promedio)

print(f"{valMin} {valMax} {promedioInt}")