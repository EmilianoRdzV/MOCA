import sys

def resolver():
    linea = sys.stdin.readline().split()
    base = float(linea[0])
    altura = float(linea[1])
    
    area = (base * altura) / 2
    
    print(f"{area}", end="")

resolver()