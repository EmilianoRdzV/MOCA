def CalcularPromedioFinal():
    try:
        # Leer las 5 calificaciones de una sola línea
        calificaciones = list(map(int, input().split()))
        
        # Calcular la suma de las calificaciones
        suma_calificaciones = sum(calificaciones)
        
        # Calcular el promedio. Como "no admite decimales",
        # usamos división entera.
        # Hay 5 exámenes.
        numero_examenes = 5 
        promedio_entero = suma_calificaciones // numero_examenes
        
        print(promedio_entero)
        
    except ValueError:
        # En caso de que la entrada no sean números o no haya 5 números.
        pass
    except Exception:
        pass

if __name__ == "__main__":
    CalcularPromedioFinal()
    