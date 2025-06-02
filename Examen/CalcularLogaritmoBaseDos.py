import math

def CalcularLogaritmoBaseDos():
    try:
        n = int(input())
        
        # Calcular el logaritmo base 2.
        # Dado que N es una potencia de 2, el resultado de math.log2(n)
        # será un número flotante que representa un entero (ej. 3.0, 5.0).
        logaritmo = math.log2(n)
        
        # Convertimos a entero para la salida.
        print(int(logaritmo))
        
    except ValueError:
        pass
    except Exception:
        pass

if __name__ == "__main__":
    CalcularLogaritmoBaseDos()