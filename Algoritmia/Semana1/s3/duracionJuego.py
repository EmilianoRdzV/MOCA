hInicio, hFin = map(int, input().split())

duracion = 0
if hFin <= hInicio:
    duracion = (24 - hInicio) + hFin
else:
    duracion = hFin - hInicio

print(duracion)