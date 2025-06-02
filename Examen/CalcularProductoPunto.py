def calcular_producto_punto():
    """
    Lee dos vectores de N componentes y calcula su producto punto.
    Luego imprime el resultado.
    """
    try:
        # 1. Leer N (cantidad de componentes)
        n = int(input())

        # 2. Leer los N enteros del primer vector (vector_a)
        vector_a = list(map(int, input().split()))

        # 3. Leer los N enteros del segundo vector (vector_b)
        vector_b = list(map(int, input().split()))

        # Pequeña validación (opcional para OmegaUp si se asume entrada perfecta)
        if len(vector_a) != n or len(vector_b) != n:
            # En un entorno real, esto sería un error.
            # Para OmegaUp, los casos de prueba suelen ser correctos.
            pass

        # 4. Calcular el producto punto
        producto_punto_resultado = 0
        for i in range(n): # Iterar n veces, desde 0 hasta n-1
            producto_componentes = vector_a[i] * vector_b[i]
            producto_punto_resultado += producto_componentes

        # Alternativa más "pythónica" para calcular el producto punto usando zip y sum:
        # producto_punto_resultado = sum(comp_a * comp_b for comp_a, comp_b in zip(vector_a, vector_b))

        # 5. Imprimir el resultado del producto punto
        print(producto_punto_resultado)

    except ValueError:
        # Si la conversión a int falla o split() no funciona como se espera.
        # Para OmegaUp, se asume entrada válida.
        pass
    except Exception as e:
        # Otra excepción inesperada.
        # print(f"Ocurrió un error: {e}")
        pass

if __name__ == "__main__":
    calcular_producto_punto()