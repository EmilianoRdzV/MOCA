def main():
    n_str = input()

    linea_numeros = input()
    lista_numeros_str = linea_numeros.split()
    lista_numeros_str.reverse()
   
    resultado = " ".join(lista_numeros_str)

    print(resultado)

if __name__ == "__main__":
    main()