import sys

n = int(sys.stdin.readline())
total = n * n
blanco = (n - 3) * (n - 3)
gris = total - blanco

print(f"{blanco} {gris}", end="")