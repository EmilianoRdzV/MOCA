def encontrar_no_fibonacci():
    """
    Encuentra y muestra todos los números enteros positivos estrictamente menores que N
    que NO pertenecen a la serie de Fibonacci.
    """
    try:
        n_limite = int(input())

        # Validar N según las consideraciones (2 <= N <= 30000)
        if not (2 <= n_limite <= 30000):
            # print("Error: N debe estar en el rango [2, 30000].")
            # En OmegaUp, se asume entrada válida; no imprimir errores no solicitados.
            return

        # Generar números de Fibonacci hasta ser mayores o iguales a N
        fibonacci_set = set()
        a, b = 1, 2 # Los dos primeros números de la serie son 1 y 2 según el problema.
        
        # Añadir los primeros números si son menores que N
        if a < n_limite:
            fibonacci_set.add(a)
        if b < n_limite: # Necesario porque el bucle empieza con el siguiente
            fibonacci_set.add(b)

        # Generar los siguientes números de Fibonacci
        # "cada número es el resultado de sumar los dos anteriores"
        # Empezamos con 1, 2. Siguiente es 1+2=3
        # El problema dice "sus primeros 2 números son 1 y 2"
        # 1, 2, 3, 5, 8, 13, 21, 34, 55...
        
        # Reiniciar a y b para la generación estándar
        a, b = 1, 2 
        while True:
            siguiente_fib = a + b
            if siguiente_fib < n_limite:
                fibonacci_set.add(siguiente_fib)
                a = b
                b = siguiente_fib
            else:
                break
        
        # Si el problema considerara que la secuencia que da Wikipedia es 0, 1, 1, 2, 3, 5...
        # pero el problema explícitamente dice "sus primeros 2 números son 1 y 2".
        # 1, 2, (1+2)=3, (2+3)=5, (3+5)=8, ...

        no_fib_numeros = []
        # Iterar por todos los números positivos estrictamente menores que N
        for i in range(1, n_limite):
            if i not in fibonacci_set:
                no_fib_numeros.append(str(i))
        
        # Imprimir los números no Fibonacci en orden creciente, separados por espacios.
        if no_fib_numeros:
            print(" ".join(no_fib_numeros))
        else:
            # Si todos los números < N son Fibonacci (ej. N=4, no-fibs: nada; N=6, no-fib: 4)
            # OmegaUp podría esperar una línea vacía o un mensaje específico.
            # " ".join([]) produce una cadena vacía, print("") imprime una línea en blanco.
            print("") # Imprime una línea vacía si no hay números no Fibonacci

    except ValueError:
        # print("Error: La entrada debe ser un número entero.")
        pass # En OmegaUp, no imprimir mensajes de error personalizados
    except Exception as e:
        # print(f"Ocurrió un error: {e}")
        pass

if __name__ == "__main__":
    encontrar_no_fibonacci()