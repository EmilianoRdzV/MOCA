a, b = map(int, input().split())

total = 0
toPrint = []

while a >= 1:
    if a % 2 != 0:
        total += b
        toPrint.append(b)
    
    a //= 2
    b *= 2

for num in toPrint:
    print(num)

print(total)