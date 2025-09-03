alturaN = int(input())

for i in range(1, alturaN + 1):
    numeroEspacios = alturaN - i
    numeroAsteriscos = 2 * i - 1
    
    espacios = " " * numeroEspacios
    asteriscos = "*" * numeroAsteriscos
    
    print(espacios + asteriscos)