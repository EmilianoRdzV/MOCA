def ProcesarNumeroN():
    """
    Lee un número N inicial, aplica tres operaciones en secuencia,
    e imprime el valor final de N y el número de veces que N fue modificado.
    """
    try:
        n_actual = int(input())
        modificaciones_count = 0

        # Restricción del problema: 1 <= N <= 1000
        # No es necesario validar aquí si se asume entrada correcta para OmegaUp.

        # --- Operación 1 ---
        n_antes_op1 = n_actual
        if n_actual % 2 == 0:  # Si N es par
            n_actual = n_actual // 2
        else:  # Si N es impar
            n_actual = n_actual + 1
        
        if n_actual != n_antes_op1:
            modificaciones_count += 1

        # --- Operación 2 ---
        n_antes_op2 = n_actual
        # Comprobar número de dígitos usando valor numérico
        if n_actual >= 100:  # Tres o más dígitos
            n_actual = n_actual // 100
        elif n_actual >= 10: # Exactamente dos dígitos (10 a 99)
            n_actual = n_actual // 10
        # Si tiene un dígito (0-9), no se hace nada según las condiciones.
        
        if n_actual != n_antes_op2:
            modificaciones_count += 1

        # --- Operación 3 ---
        n_antes_op3 = n_actual
        if n_actual % 3 == 0:  # Si N es múltiplo de tres
            n_actual = n_actual - 1
            
        if n_actual != n_antes_op3:
            modificaciones_count += 1

        # Salida: valor final de N y número de modificaciones
        print(n_actual, modificaciones_count)

    except ValueError:
        # Manejo si la entrada no es un entero.
        pass
    except Exception as e:
        # Otro error.
        pass

if __name__ == "__main__":
    ProcesarNumeroN()