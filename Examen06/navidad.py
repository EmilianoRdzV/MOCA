n = int(input())

numFollaje = n

# El ancho maximo lo da la ultima linea de follaje
# (la linea en el indice n-1)
anchoMax = 2 * (numFollaje - 1) + 1

# follaje (N lineas)
for i in range(numFollaje):
    numEstrellas = 2 * i + 1
    estrellas = '*' * numEstrellas
    print(estrellas.center(anchoMax))

# tronco (2 lineas)
tronco = '###'
print(tronco.center(anchoMax))
print(tronco.center(anchoMax))