def convertir_binario_a_decimal():
    """
    Lee una cadena binaria de 31 bits y la convierte a decimal
    según las reglas especificadas (normal si empieza con 0,
    complemento a dos si empieza con 1).
    """
    cadena_binaria = input()
    numero_de_bits = 31

    if len(cadena_binaria) != numero_de_bits:
        # Esto no debería ocurrir según las restricciones ("La cadena siempre tendrá 31 bits")
        # pero es una comprobación de robustez. En OmegaUp, se asume entrada válida.
        # print("Error: La cadena no tiene 31 bits.")
        return

    primer_bit = cadena_binaria[0]
    valor_decimal = 0

    if primer_bit == '0':
        # Es un número positivo, conversión binaria normal.  
        valor_decimal = int(cadena_binaria, 2)
    else: # El primer_bit es '1', es un número negativo en complemento a dos.
        # Método 1: Calcular el valor sin signo y restar 2^numero_de_bits
        valor_sin_signo = int(cadena_binaria, 2)
        valor_decimal = valor_sin_signo - (1 << numero_de_bits)


    print(valor_decimal)

if __name__ == "__main__":
    convertir_binario_a_decimal()