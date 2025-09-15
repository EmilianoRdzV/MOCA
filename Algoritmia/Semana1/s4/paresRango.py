n = int(input())
m = int(input())

pares = []


for i in range(n, m + 1):  
    if i % 2 == 0:
        pares.append(i)
        print(i)
         

         