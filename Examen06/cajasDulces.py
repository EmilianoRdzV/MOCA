lineaNK = input().split()
n = int(lineaNK[0])
k = int(lineaNK[1])

lineaCajas = input().split()
cajas = [int(num) for num in lineaCajas]

# Calcular la suma de la primera ventana (de 0 a k-1)
sumaActual = sum(cajas[0:k])
sumaMax = sumaActual

# Deslizar la ventana
# El rango va desde el indice 1 hasta (n - k)
for i in range(1, n - k + 1):
    
    # i es el nuevo indice de inicio
    elemSale = cajas[i - 1]      # Elemento que sale (a la izquierda)
    elemEntra = cajas[i + k - 1] # Elemento que entra (a la derecha)
    
    # Actualizamos la suma actual de forma eficiente
    sumaActual = sumaActual - elemSale + elemEntra
    
    if sumaActual > sumaMax:
        sumaMax = sumaActual

print(sumaMax)