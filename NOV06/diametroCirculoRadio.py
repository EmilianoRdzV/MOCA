import sys
import math

s = float(sys.stdin.readline())
pi = math.pi

r = math.sqrt(s / pi)
d = 2.0 * r
p = 2.0 * pi * r

print(f"{d:.2f} {r:.2f} {p:.2f}", end="")
