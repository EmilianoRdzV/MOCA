numeroDeCartas = int(input())
listaCartas = list(map(int, input().split()))

sumaAparicio = 0
conteoAparicio = 0
sumaNonila = 0
conteoNonila = 0

for carta in listaCartas:
    if carta % 2 == 0:
        sumaAparicio += carta
        conteoAparicio += 1
    else:
        sumaNonila += carta
        conteoNonila += 1

promedioAparicio = 0
if conteoAparicio > 0:
    promedioAparicio = sumaAparicio // conteoAparicio

promedioNonila = 0
if conteoNonila > 0:
    promedioNonila = sumaNonila // conteoNonila

if promedioAparicio > promedioNonila:
    print("APARICIO")
elif promedioNonila > promedioAparicio:
    print("NONILA")
else:
    print("EMPATE!")