import sys
a, b = map(int, sys.stdin.readline().split())

# abs() es la función de valor absoluto 
diferencia = abs(a - b)

print(diferencia, end="")