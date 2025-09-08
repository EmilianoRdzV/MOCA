n = int(input())

pasos = 0
maxVal = n

while n != 1:
    if n % 2 == 0:
        n = n // 2
    else:
        n = 3 * n + 1
    
    pasos += 1
    
    if n > maxVal:
        maxVal = n

print(pasos, maxVal)