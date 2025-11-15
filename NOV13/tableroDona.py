def resolver():
    linea = list(map(int, input().split()))
    
    ancho = linea[0]
    alto = linea[1]
    posX = linea[2]
    posY = linea[3]
    movH = linea[4]
    movV = linea[5]
    
    # % maneja negativos correctamente
    resX = (posX + movH) % ancho
    resY = (posY + movV) % alto
    
    print(f"{resX} {resY}")

resolver()