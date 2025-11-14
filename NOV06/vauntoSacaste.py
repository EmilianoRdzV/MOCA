import sys

n = int(sys.stdin.readline())

for _ in range(3):
    amigoScore = int(sys.stdin.readline())
    if n > amigoScore:
        print("Soy Mejor")
    elif n < amigoScore:
        print("Shh")
    else:
        print("Te gano en la siguiente")
