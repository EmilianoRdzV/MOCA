def ordenarCalificaciones():
    try:
        cantidadAlumnos = int(input())
        calificaciones = list(map(int, input().split()))
    except (ValueError, IndexError):
        return

    calificaciones.sort(reverse=True)

    print(" ".join(map(str, calificaciones)))

if __name__ == "__main__":
    ordenarCalificaciones()