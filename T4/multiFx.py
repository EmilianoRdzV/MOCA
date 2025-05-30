def calcular_producto_de_diferencias():
    """
    Lee cuatro variables enteras A, B, C y D.
    Calcula e imprime la multiplicación de la diferencia de A y B
    con la diferencia de C y D.
    Fórmula: (A - B) * (C - D)
    """
    try:
        # Leer los cuatro enteros A, B, C y D de la misma línea,
        # separados por espacios.
        a, b, c, d = map(int, input().split())

        # Calcular la diferencia entre A y B.
        diferencia_ab = a - b

        # Calcular la diferencia entre C y D.
        diferencia_cd = c - d

        # Calcular la multiplicación de ambas diferencias.
        resultado = diferencia_ab * diferencia_cd

        # Imprimir el resultado.
        print(resultado)

    except ValueError:
        # Esto se manejaría si la entrada no son cuatro números enteros válidos
        # o si no hay suficientes números.
        # En un entorno competitivo, usualmente se asume entrada válida.
        # print("Entrada inválida. Por favor ingrese cuatro números enteros separados por espacio.")
        pass # No imprimir mensajes de error no solicitados en OmegaUp.
    except Exception as e:
        # Captura de cualquier otra excepción inesperada.
        # print(f"Ocurrió un error inesperado: {e}")
        pass

if __name__ == "__main__":
    calcular_producto_de_diferencias()