n = int(input())
conjuntoNum = set()

for _ in range(n):
    conjuntoNum.add(int(input()))

numBuscar = int(input())

if numBuscar in conjuntoNum:
    print("Si")
else:
    print("No")