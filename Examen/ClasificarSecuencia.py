def ClasificarSecuencia():
    try:
        a, b, c = map(int, input().split())

        # Primero, verificar la condición de mayor prioridad: todos iguales
        if a == b and b == c:
            print("I")
        # Luego, verificar si es creciente débil (y no todos iguales, ya cubierto arriba)
        elif a <= b and b <= c:
            print("C")
        # Luego, verificar si es decreciente débil (y no todos iguales, ya cubierto arriba)
        elif a >= b and b >= c:
            print("D")
        # Si ninguna de las anteriores condiciones se cumple
        else:
            print("X")
            
    except ValueError:
        # Manejo de error si la entrada no son números
        pass 
    except Exception:
        # Manejo de otros errores inesperados
        pass

if __name__ == "__main__":
    ClasificarSecuencia()