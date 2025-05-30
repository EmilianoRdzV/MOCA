def CalculoAsientos():
    """
    Calcula cuántas personas estarán sentadas y cuántas de pie en un concierto.
    """
    try:
        # Leer la primera línea: número de filas (r) y asientos por fila (s)
        r, s = map(int, input().split())

        # Leer la segunda línea: número de boletos vendidos (b)
        b = int(input())

        # Validar las restricciones (opcional para OmegaUp si se asume entrada válida,
        # pero buena práctica considerarlas).
        # 0 <= r <= 10,000
        # 0 <= s <= 10,000
        # b >= 0 (asumido, ya que es número de boletos)
        if not (0 <= r <= 10000 and 0 <= s <= 10000 and b >= 0):
            # En un entorno competitivo, normalmente no se imprimen mensajes de error
            # a menos que el problema lo especifique.
            # Si la entrada viola las restricciones, el comportamiento puede ser indefinido
            # o el juez puede proveer entradas que siempre las cumplen.
            # Para este ejemplo, asumiremos que la entrada es válida.
            pass

        # Calcular el número total de asientos disponibles
        total_asientos = r * s

        # Determinar cuántas personas se pueden sentar
        personas_sentadas = 0
        if total_asientos >= b:
            # Si hay suficientes asientos para todos los que tienen boleto
            personas_sentadas = b
        else:
            # Si no hay suficientes asientos, solo se sientan los que caben
            personas_sentadas = total_asientos
    
        personas_paradas = b - personas_sentadas
        print(personas_sentadas, personas_paradas)

    except ValueError:
        # Manejo de error si la entrada no puede ser convertida a entero.
        # En OmegaUp, se asume que la entrada tendrá el formato correcto.
        # print("Error: Entrada inválida. Asegúrese de ingresar números enteros.")
        pass
    except Exception as e:
        # Otro tipo de error inesperado.
        # print(f"Ocurrió un error inesperado: {e}")
        pass

if __name__ == "__main__":
    CalculoAsientos()