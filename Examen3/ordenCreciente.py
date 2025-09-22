n = int(input())
listaOriginal = list(map(int, input().split()))

listaOrdenada = sorted(listaOriginal)

if listaOriginal == listaOrdenada:
    print("SI")
else:
    print("NO")