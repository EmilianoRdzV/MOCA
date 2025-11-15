n = int(input())

if n == 0:
    print(0)
else:
    
    nums = list(map(int, input().split()))
    
    # up = Longitud max. terminando en un AUMENTO
    # down = Longitud max. terminando en una CAÍDA
    # Cualquier número por sí solo es una subsecuencia de longitud 1
    up = 1
    down = 1
    
    # Empezar a comparar desde el segundo elemento
    for i in range(1, n):
        # Calcular la diferencia con el número anterior
        diferencia = nums[i] - nums[i-1]
        
        if diferencia > 0:
            # Hay un AUMENTO
            # Esto solo puede extender una secuencia que terminó en CAÍDA.
            up = down + 1
            
        elif diferencia < 0:
            # Esto solo puede extender una secuencia que terminó en AUMENTO.
            down = up + 1
            
    print(max(up, down))