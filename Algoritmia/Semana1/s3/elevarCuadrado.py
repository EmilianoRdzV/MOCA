numeroInicial = int(input())
conteo = 0

while numeroInicial < 30000:
    numeroInicial = numeroInicial * numeroInicial
    conteo += 1

print(f"{numeroInicial} {conteo}")