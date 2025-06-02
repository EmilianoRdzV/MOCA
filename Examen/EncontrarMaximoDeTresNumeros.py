def EncontrarMaximoDeTresNumeros():
    try:
        a, b, c = map(int, input().split())
        maximo_valor = max(a, b, c)
        print(maximo_valor)
    except (ValueError, IndexError):
        # Manejo básico de errores si la entrada no es válida.
        # Para OmegaUp, si se garantiza entrada correcta, esto podría omitirse.
        pass 

if __name__ == "__main__":
    EncontrarMaximoDeTresNumeros()