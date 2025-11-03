import sys

n = int(sys.stdin.readline())
sedes = []

for _ in range(n):
    sedes.append(int(sys.stdin.readline()))


minSede = min(sedes)
maxSede = max(sedes)

print(maxSede - minSede)