frecuenciaActual = int(input())

if frecuenciaActual < 540 or frecuenciaActual > 1520:
    print("error")
else:
    frecuenciasEstaciones = [580, 980, 1190, 1250, 1420]
    
    frecuenciaMasCercana = -1
    diferenciaMinima = float('inf')

    for frecuenciaEstacion in frecuenciasEstaciones:
        diferencia = abs(frecuenciaActual - frecuenciaEstacion)
        
        if diferencia < diferenciaMinima:
            diferenciaMinima = diferencia
            frecuenciaMasCercana = frecuenciaEstacion
        elif diferencia == diferenciaMinima:
            if frecuenciaEstacion > frecuenciaMasCercana:
                frecuenciaMasCercana = frecuenciaEstacion
    
    direccion = "atras"
    if frecuenciaMasCercana > frecuenciaActual:
        direccion = "adelante"
        
    print(f"{direccion} {diferenciaMinima}")