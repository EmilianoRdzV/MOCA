def CalcularBolitasDeAristoteles():
    try:
        # Leer la cantidad de bolitas que agarró Frodo
        bolitas_frodo = int(input())

        # Calcular cuántas bolitas agarró Cortázar
        # Cortázar tomó el triple de bolitas que Frodo
        bolitas_cortazar = 3 * bolitas_frodo

        # Calcular cuántas bolitas agarró Aristóteles
        # Aristóteles agarró 2 bolitas más que Cortázar
        bolitas_aristoteles = bolitas_cortazar + 2

        # Imprimir la cantidad de bolitas que agarró Aristóteles
        print(bolitas_aristoteles)

    except ValueError:
        # Manejo en caso de que la entrada no sea un entero.
        # Para OmegaUp, si se garantiza entrada válida, esto podría omitirse.
        pass
    except Exception as e:
        # Otro error inesperado.
        pass

if __name__ == "__main__":
    CalcularBolitasDeAristoteles()