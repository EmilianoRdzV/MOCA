def resolver():
    n = int(input())
    num_bits = 24

    if n >= 0:
        # Para números positivos (y cero):
        # Convertir a binario normal y rellenar con ceros a la izquierda hasta 24 bits.
        # El rango de entrada es hasta 2^23.
        # bin(2^23) es '0b1' seguido de 23 ceros, lo que son 24 bits en total.
        # format(n, '024b') maneja esto correctamente.
        # Por ejemplo, format(2**23, '024b') da '100000000000000000000000'.
        # format(2**23 - 1, '024b') da '011111111111111111111111'.
        resultado_binario = format(n, f'0{num_bits}b')
        
        # Asegurarnos de que no exceda los num_bits, aunque con el rango dado no debería.
        # La especificación de formato '0Nb' si el número es muy grande puede dar más de N bits.
        # Sin embargo, el máximo n (2^23) cabe exactamente en 24 bits.
        if len(resultado_binario) > num_bits:
             # Esto no debería ocurrir con las restricciones del problema [-2^23, 2^23]
             # para números positivos. 2^23 es 1 seguido de 23 ceros (24 bits).
             # Si n fuera 2^24, format(n, '024b') daría 25 bits.
             # Pero n está limitado a 2^23.
            resultado_binario = resultado_binario[-num_bits:]

        print(resultado_binario)
    else:
        # Para números negativos: calcular complemento a dos.
        # El método es: 2^num_bits - abs(n), o equivalentemente (1 << num_bits) + n
        # (ya que n es negativo).
        # El resultado de esta operación será un número positivo, cuya representación
        # binaria de 'num_bits' es el complemento a dos de n.
        
        # Ejemplo: n = -50, num_bits = 24
        # (1 << 24) + (-50) = 16777216 - 50 = 16777166
        # bin(16777166) es '0b111111111111111111001110'
        # format(16777166, '024b') da '111111111111111111001110'

        # El número negativo más pequeño en el rango es -2^23.
        # (1 << 24) + (-2**23) = 2**24 - 2**23 = 2**23.
        # format(2**23, '024b') da '100000000000000000000000', que es correcto para -2^23 C2.
        
        valor_para_conversion = (1 << num_bits) + n
        resultado_binario = format(valor_para_conversion, f'0{num_bits}b')
        print(resultado_binario)

if __name__ == "__main__":
    resolver()