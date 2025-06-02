def decidir_hueso():
    """
    Ayuda a determinar qué hueso comprar para el perrito,
    basándose en el olor y el tamaño de dos huesos.
    """
    try:
        # Leer los atributos del Hueso 1 (L1: olor, T1: tamaño)
        l1, t1 = map(int, input().split())

        # Leer los atributos del Hueso 2 (L2: olor, T2: tamaño)
        l2, t2 = map(int, input().split())

        # Validar restricciones (1 <= L, T <= 10)
        # En OmegaUp, usualmente se asume que la entrada cumple con los límites.
        # if not (1 <= l1 <= 10 and 1 <= t1 <= 10 and \
        #         1 <= l2 <= 10 and 1 <= t2 <= 10):
        #     # Manejar error si es necesario, pero para OmegaUp no imprimir mensajes no solicitados
        #     return

        # Determinar si el Hueso 1 es el mejor en ambos criterios
        # "simultáneamente el más grande y el que huele mejor"
        # El problema también indica "los dos huesos difieren en olor y también difieren en tamaño",
        # por lo que no necesitamos preocuparnos por empates (L1=L2 o T1=T2).

        es_hueso1_el_mejor_en_olor = (l1 > l2)
        es_hueso1_el_mas_grande = (t1 > t2)

        es_hueso2_el_mejor_en_olor = (l2 > l1)
        es_hueso2_el_mas_grande = (t2 > t1)

        if es_hueso1_el_mas_grande and es_hueso1_el_mejor_en_olor:
            print("Hueso 1")
        elif es_hueso2_el_mas_grande and es_hueso2_el_mejor_en_olor:
            print("Hueso 2")
        else:
            # Esto ocurre si un hueso es más grande pero el otro huele mejor,
            # o viceversa.
            print("Perrito confundido :(")

    except ValueError:
        # Esto ocurriría si la entrada no puede ser convertida a enteros
        # o si no hay dos números en una línea.
        # En OmegaUp, usualmente se asume que la entrada es válida.
        # print("Error: Entrada inválida. Se esperaban dos números enteros por línea.")
        pass
    except Exception as e:
        # Captura de cualquier otra excepción inesperada.
        # print(f"Ocurrió un error inesperado: {e}")
        pass

if __name__ == "__main__":
    decidir_hueso()