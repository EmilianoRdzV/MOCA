def resolver():
    totalSeg = int(input())
    
    # tiempo en segundos
    segEnMin = 60
    segEnHora = 3600
    segEnDia = 86400
    segEnAno = 31536000
 
    resA = totalSeg // segEnAno
    totalSeg %= segEnAno
    
    resD = totalSeg // segEnDia
    totalSeg %= segEnDia
    
    resH = totalSeg // segEnHora
    totalSeg %= segEnHora
    
    resM = totalSeg // segEnMin
    totalSeg %= segEnMin
    
    resQ = totalSeg
    
    print(f"{resA} {resD} {resH} {resM} {resQ}")

resolver()