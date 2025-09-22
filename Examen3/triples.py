n = int(input())

tripleIndices = []

for i in range(n):
    num = int(input())
    if num % 3 == 0:
        tripleIndices.append(i + 1)

if len(tripleIndices) > 0:
    print(len(tripleIndices))
    print(*tripleIndices)
else:
    print("No hay triples..")