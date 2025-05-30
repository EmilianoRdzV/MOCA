def valorAbsoluto():
    """
    Lee dos enteros M y N, calcula la suma de ambos,
    y luego imprime el valor absoluto de esa suma.
    """
    try:
        # Leer los dos enteros M y N de la misma línea, separados por un espacio.
        # input().split() divide la cadena de entrada por espacios.
        # map(int, ...) aplica la función int a cada parte.
        m, n = map(int, input().split())

        # Validar que M y N estén dentro de los límites especificados (-1000 a 1000).
        # Para OmegaUp y problemas similares, a menudo se asume que la entrada
        # cumplirá con los límites, por lo que esta validación explícita
        # podría omitirse si no se requieren mensajes de error específicos.
        if not (-1000 <= m <= 1000 and -1000 <= n <= 1000):
            # En un entorno competitivo, no se suelen imprimir mensajes de error
            # a menos que se especifique. Se asume entrada válida.
            # Si la entrada está fuera de los límites y se procesa,
            # el resultado aún podría ser matemáticamente correcto.
            pass # Asumimos que OmegaUp proveerá entradas dentro de los límites.

        # Calcular la suma de M y N.
        suma = m + n

        # Calcular el valor absoluto de la suma.
        valor_abs = abs(suma)

        # Imprimir el resultado.
        print(valor_abs)

    except ValueError:
        # Esto se activaría si la entrada no son dos números enteros válidos.
        # En un entorno competitivo, usualmente se asume entrada válida.
        # print("Entrada inválida. Por favor ingrese dos números enteros separados por espacio.")
        pass # No hacer nada o simplemente dejar que el programa falle si la entrada es incorrecta.
    except Exception as e:
        # Captura de cualquier otra excepción inesperada.
        # print(f"Ocurrió un error inesperado: {e}")
        pass

if __name__ == "__main__":
    valorAbsoluto()