import math
import sys

n = int(sys.stdin.readline())

for x in range(1, n + 1):
    fx = math.exp(2 * x) - x
    print(f"{x} {fx:.3f}")
