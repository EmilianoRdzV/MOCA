import sys

n = int(sys.stdin.readline())
resultados = list(map(int, sys.stdin.readline().split()))

maryWins = resultados.count(0)

johnWins = resultados.count(1)

print(f"Mary won {maryWins} times and John won {johnWins} times", end="")