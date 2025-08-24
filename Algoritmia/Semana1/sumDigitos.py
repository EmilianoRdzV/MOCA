def sumarDigitos(numero):
    if numero < 10:
        return numero
    else:
        return (numero % 10) + sumarDigitos(numero // 10)

numeroEntrada = int(input())
resultado = sumarDigitos(numeroEntrada)
print(resultado)