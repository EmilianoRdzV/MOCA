import collections
import sys

lector = sys.stdin.readline

lineaInicial = lector().split()
comidaTotal = int(lineaInicial[0])
numAcciones = int(lineaInicial[1])

filaCanguros = collections.deque()

for _ in range(numAcciones):
    
    lineaAccion = lector().split()
    accion = lineaAccion[0]
    
    # Acción N: Nuevo canguro
    if accion == 'N':
        numPequeños = int(lineaAccion[1])
        filaCanguros.append(numPequeños)
        
    # Acción A: Atender canguro 
    elif accion == 'A':
        # Sacar al primer canguro de la fila
        numPequeños = filaCanguros.popleft()
        
        # Calcular costo (1 grande + N pequeños)
        costoComida = 1 + numPequeños
        
        # Restar la comida
        comidaTotal -= costoComida
        
    # Acción C: Contar canguros ---
    elif accion == 'C':
        print(len(filaCanguros))
        
    # Acción R: Comida Restante ---
    elif accion == 'R':
        print(comidaTotal)