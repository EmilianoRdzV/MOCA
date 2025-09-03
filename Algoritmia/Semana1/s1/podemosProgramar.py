def calcularY():
    try:
        x = float(input())
    except (ValueError, IndexError):
        return

    terminoComun = (x + x**2) / (5*x + 3)
    
    # Esta es la línea clave corregida
    y = terminoComun * (terminoComun + x) / (terminoComun + 2*x)

    print(y)

if __name__ == "__main__":
    calcularY()