a,b,c = input().split()

a = int(a)
b = int(b)
c = float(c)

codigo2, unidades2, precio2 = input().split()
codigo2 = int(codigo2)
unidades2 = int(unidades2)
precio2 = float(precio2)


total = ((c*b)+ (unidades2*precio2))
print(f"{total:.2f}")