import sys

mapa = {")": "(", "}": "{", "]": "["}
t = int(sys.stdin.readline())
salida = []

for _ in range(t):
    s = sys.stdin.readline().strip()
    pila = []
    balanceado = True
    for c in s:
        if c in "({[":
            pila.append(c)
        elif c in ")}]":
            if not pila or pila.pop() != mapa[c]:
                balanceado = False
                break
    if balanceado and not pila:
        salida.append("SI")
    else:
        salida.append("NO")

print("\n".join(salida))
