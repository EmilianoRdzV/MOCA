numeroProfesores, numeroAlumnos = map(int, input().split())
votos = list(map(int, input().split()))

conteoVotos = [0] * (numeroProfesores + 1)

for voto in votos:
    conteoVotos[voto] += 1

for profesorId in range(1, numeroProfesores + 1):
    print(f"{profesorId}-{conteoVotos[profesorId]}")