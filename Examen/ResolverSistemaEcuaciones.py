def ResolverSistemaEcuaciones():
    try:
        # Leer coeficientes de la primera ecuación
        a1, b1, c1 = map(float, input().split())
        
        # Leer coeficientes de la segunda ecuación
        a2, b2, c2 = map(float, input().split())
        
        # Calcular el determinante principal
        determinante_principal = (a1 * b2) - (a2 * b1)
        
        # Calcular determinantes para x e y
        determinante_x = (c1 * b2) - (c2 * b1)
        determinante_y = (a1 * c2) - (a2 * c1)
        
        # Calcular x e y
        # El problema garantiza una única solución, por lo que D no será 0.
        x = determinante_x / determinante_principal
        y = determinante_y / determinante_principal
        
        # Imprimir la solución formateada.
        # El ejemplo muestra 6 decimales.
        print(f"{x:.6f} {y:.6f}")
        
    except ValueError:
        # Manejo de error si la entrada no son números flotantes válidos
        pass
    except ZeroDivisionError:
        # Aunque el problema garantiza D != 0, es buena práctica considerarlo.
        # En este contexto, no debería ocurrir según las especificaciones.
        pass
    except Exception:
        # Manejo de otros errores inesperados
        pass

if __name__ == "__main__":
    ResolverSistemaEcuaciones()