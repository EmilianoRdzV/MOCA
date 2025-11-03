import sys

n = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))

a, b = map(int, sys.stdin.readline().split())

conteo = 0

for num in nums:
    if num >= a and num <= b:
        conteo += 1

print(conteo, end="")