n, m = map(int, input().split())

a = n // m
b = n % m

if b == 0:
    print(a)
else:
    print(f"{a} {b}/{m}")