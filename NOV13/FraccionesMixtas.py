N, D = map(int, input().split())

entero = N // D       
residuo = N % D       

if residuo == 0:
    print(entero)
elif entero == 0:
    print(f"{residuo}/{D}")
else:
    print(f"{entero} {residuo}/{D}")
