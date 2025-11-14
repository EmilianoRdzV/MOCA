import sys

for linea in sys.stdin:
    linea = linea.strip()
    if not linea:
        continue  # salta líneas vacías
    # dividir por coma o espacio
    partes = linea.replace(',', ' ').split()
    if len(partes) < 2:
        continue

    clave = int(partes[0])
    numin = float(partes[1])

    if clave == 12:
        precio = 2.0
    elif clave == 15:
        precio = 2.2
    elif clave == 18:
        precio = 4.5
    elif clave == 19:
        precio = 3.5
    elif clave == 23:
        precio = 6.0
    elif clave == 25:
        precio = 6.0
    elif clave == 29:
        precio = 5.0
    else:
        precio = 0.0

    costoTotal = precio * numin

    # imprime sin ceros extra ni punto decimal si no hace falta
    print(f"{costoTotal:g}")
