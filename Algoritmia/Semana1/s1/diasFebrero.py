listaAños = list(map(int, input().split()))

for anio in listaAños:
    esBisiesto = (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0)
    
    if esBisiesto:
        print(29)
    else:
        print(28)