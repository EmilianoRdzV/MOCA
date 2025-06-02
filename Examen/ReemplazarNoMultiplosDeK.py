def ReemplazarNoMultiplosDeK():
    """
    Lee una secuencia de N enteros y un entero K.
    Reimprime la secuencia, reemplazando los enteros que no son múltiplos de K 
    por una 'X' mayúscula.
    """
    try:
        # Leer N
        n_elementos = int(input())

        secuencia_numeros = []
        if n_elementos > 0:
            secuencia_numeros = list(map(int, input().split()))
        # Si n_elementos es 0, secuencia_numeros permanecerá vacía.

        # Leer K
        k = int(input())

        elementos_salida = []

        if k <= 0: # Manejo defensivo para K no positivo
            # Si K no es positivo, ningún número (del rango 1-100) se considerará múltiplo en el sentido común.
            # Así que todos los números de la secuencia serían 'X'.
            for _ in secuencia_numeros:
                elementos_salida.append("X")
        else:
            for numero in secuencia_numeros:
                if numero % k == 0:  # Es múltiplo de K
                    elementos_salida.append(str(numero))
                else:  # No es múltiplo de K
                    elementos_salida.append("X")
        
    
        print(" ".join(elementos_salida))

    except ValueError:
    
        pass
    except Exception as e:
        # Cualquier otro error inesperado.
        pass

if __name__ == "__main__":
    ReemplazarNoMultiplosDeK()