import sys
sys.setrecursionlimit(2000)

class Nodo:
    def __init__(self, val):
        self.valor = val
        self.izq = None
        self.der = None

def construirArbol(sec):
    if not sec:
        return None
     
    # La raíz es el último elemento
    valRaiz = sec[-1]
    nodo = Nodo(valRaiz)
    
    secIzq = []
    secDer = []
    
    # Particiona el resto de la secuencia
    for i in range(len(sec) - 1):
        if sec[i] < valRaiz:
            secIzq.append(sec[i])
        else:
            secDer.append(sec[i])
            
    nodo.izq = construirArbol(secIzq)
    nodo.der = construirArbol(secDer)
    
    return nodo

def preorden(nodo, res):
    if nodo is None:
        return
    
    res.append(str(nodo.valor))
    preorden(nodo.izq, res)
    preorden(nodo.der, res)

def resolver():
    n = int(input())
    secRem = list(map(int, input().split()))
    
    raiz = construirArbol(secRem)
    
    resPreorden = []
    preorden(raiz, resPreorden)
    
    print(" ".join(resPreorden))

resolver()