meses = [
    "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
    "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"
]

N = int(input())

for _ in range(N):
    M = int(input())
    if 1 <= M <= 12:
        print(meses[M - 1])
    else:
        print("Error")