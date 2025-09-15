import math
p, s, r = map(int, input().split())

if s >= p:
    d = 1  
else:
    d = math.ceil((p - s) / (s - r)) + 1

print(d)