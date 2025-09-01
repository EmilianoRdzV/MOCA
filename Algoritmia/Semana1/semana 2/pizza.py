n, m, k = map(int, input().split())
pizzas_g = k
pizzas_c = m // 2 + m % 2

sobrante = (pizzas_g * 1) * 0.25
if m % 2 == 1:
    sobrante += 0.5  

cuartos_puebla = n

cuartos_disponibles = int(sobrante * 4)

if cuartos_disponibles >= cuartos_puebla:
    pizzas_p = 0
else:
    faltan = cuartos_puebla - cuartos_disponibles
    pizzas_p = (faltan + 3) // 4  

print(pizzas_g + pizzas_c + pizzas_p)