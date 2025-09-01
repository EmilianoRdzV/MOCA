llamadas = 0

def fibonacci(n):
    global llamadas
    llamadas += 1

    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

N = int(input())
resultado = fibonacci(N)
print(resultado, llamadas)
