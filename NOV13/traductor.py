def resolver():
    lineaUno = input().split()
    numDic = int(lineaUno[0])
    numPal = int(lineaUno[1])
    
    dic = {}
    for _ in range(numDic):
        lineaDic = input().split()
        llave = int(lineaDic[0])
        valor = int(lineaDic[1])
        dic[llave] = valor
        
    resultados = []
    for _ in range(numPal):
        palNum = int(input())
        
        # .get() busca la llave y retorna un valor por defecto si no la encuentra
        traduccion = dic.get(palNum, "C?")
        resultados.append(str(traduccion))
        
    print("\n".join(resultados))

resolver()