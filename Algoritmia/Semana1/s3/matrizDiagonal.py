n = int(input())

diagonal = []
for i in range(n):
    row = list(map(int, input().split()))
    diagonal.append(row[i])

if n == 0:
    print("SI") 
elif len(set(diagonal)) == 1:
    print("SI")
else:
    print("NO")