f, c = map(int, input().split())

matrix = []
for _ in range(f):
    row = list(map(int, input().split()))
    matrix.append(row)

for row in reversed(matrix):
    print(*row)