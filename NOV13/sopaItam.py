def resolver():
    sopaLetras = input()
    
    conteo = {}
    for char in sopaLetras:
        conteo[char] = conteo.get(char, 0) + 1
        
    vecesM = conteo.get('m', 0)
    vecesI = conteo.get('i', 0)
    vecesG = conteo.get('g', 0)
    vecesU = conteo.get('u', 0)
    vecesE = conteo.get('e', 0)
    vecesL = conteo.get('l', 0)
    
    resultado = min(vecesM, vecesI, vecesG, vecesU, vecesE, vecesL)
    
    print(resultado)

resolver()