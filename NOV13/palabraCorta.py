def resolver():
    n = int(input())
    
    palabraCorta = ""
    longitudCorta = 501
    
    for _ in range(n):
        palabraActual = input()
        longitudActual = len(palabraActual)
        
        if longitudActual < longitudCorta:
            longitudCorta = longitudActual
            palabraCorta = palabraActual
            
    paridad = "par" if longitudCorta % 2 == 0 else "impar"
    
    print(palabraCorta)
    print(longitudCorta)
    print(paridad)

resolver()