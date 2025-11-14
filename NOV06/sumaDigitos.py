import sys

linea = sys.stdin.readline().strip()
n = linea.strip()

suma = sum(int(digito) for digito in n)

print(suma)
