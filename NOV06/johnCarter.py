
lineaCostos = input().split()
p = int(lineaCostos[0])  # Costo plano '-'
s = int(lineaCostos[1])  # Costo subida '/'
b = int(lineaCostos[2])  # Costo bajada '\'

terreno = input()

tiempoTotal = 0

# Iterar por cada tramo del terreno
for tramo in terreno:
    if tramo == '-':
        tiempoTotal += p
    elif tramo == '/':
        tiempoTotal += s
    elif tramo == '\\':
        tiempoTotal += b

print(tiempoTotal)