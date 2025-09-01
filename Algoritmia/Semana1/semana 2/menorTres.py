a = int(input())
b = int(input())
c = int(input())

menor = a
if b < menor:
    menor = b
if c < menor:
    menor = c

print(menor)
