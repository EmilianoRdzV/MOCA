def CalcularSumaSimple():
    try:
        # Leer los dos números enteros de una sola línea
        a, b = map(int, input().split())
        
        # Calcular la suma
        resultado = a + b
        
        # Imprimir el resultado
        print(resultado)
        
    except ValueError:
        # En caso de que la entrada no sea la esperada
        pass
    except Exception:
        pass

if __name__ == "__main__":
    CalcularSumaSimple()