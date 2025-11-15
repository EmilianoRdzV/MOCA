def resolver():
    n = int(input())

    conteoDigitos = [0] * 10
    
    for _ in range(n):
        linea = input()
        for char in linea:
            if char.isdigit():
                digito = int(char)
                conteoDigitos[digito] += 1
                
    for i in range(10):
        print(f"El {i} aparece {conteoDigitos[i]} veces.")

resolver()