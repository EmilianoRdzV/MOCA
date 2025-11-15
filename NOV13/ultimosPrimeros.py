nombres = []

while True:
    nombre = input()
    
    if nombre == "#":
        break  
    
    nombres.append(nombre)

for nombre in reversed(nombres):
    print(nombre)