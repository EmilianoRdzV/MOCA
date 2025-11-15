
linea = input().split()
i = int(linea[0])
d = int(linea[1])

rueda = [1, 2, 3, 4, 5]

netGirosIzquierda = (i - d) % 5

resultado = rueda[netGirosIzquierda:] + rueda[:netGirosIzquierda]

print(" ".join(map(str, resultado)))