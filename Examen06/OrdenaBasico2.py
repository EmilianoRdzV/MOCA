import sys

n = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
nums.sort(reverse=True)

salida = []
for num in nums:
    salida.append(str(num))

print("\n".join(salida))
