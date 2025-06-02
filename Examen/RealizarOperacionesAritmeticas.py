def RealizarOperacionesAritmeticas():
    try:
        # Leer los dos enteros a y b de una sola línea, separados por un espacio
        a, b = map(int, input().split())

        # Realizar las operaciones en el orden especificado
        suma = a + b
        resta = a - b
        
        # Para división entera y módulo, es importante considerar si b puede ser 0.
        # Si las restricciones del problema garantizan b != 0, no se necesita manejo especial.
        # Si b puede ser 0, se necesitaría definir el comportamiento (ej. imprimir error o un valor específico).
        # Asumiremos aquí que b != 0 según el uso típico de estas operaciones en problemas.
        division_entera = a // b  # División entera en Python
        multiplicacion = a * b
        modulo = a % b            # Operador módulo en Python

        # Imprimir los resultados en una sola línea, separados por un espacio.
        # print() con múltiples argumentos los separa por espacio por defecto.
        print(suma, resta, division_entera, multiplicacion, modulo)

    except ValueError:
        # Ocurre si la entrada no puede ser convertida a enteros
        # o si no hay exactamente dos números.
        # En OmegaUp, si se garantiza entrada válida, este bloque puede omitirse.
        pass
    except ZeroDivisionError:
        # Ocurre si b es 0 en la división o módulo.
        # print("Error: No se puede dividir por cero.") # No imprimir en OmegaUp a menos que se pida.
        pass
    except Exception as e:
        # Otros errores inesperados.
        pass

if __name__ == "__main__":
    RealizarOperacionesAritmeticas()