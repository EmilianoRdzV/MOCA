def convertFija(expresion):
 
  #Convertir de infija a postfija
    precedencia = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    pila = []
    salida_postfija = []
    
    for caracter in expresion:
        if 'A' <= caracter <= 'Z': # Operando
            salida_postfija.append(caracter)
        elif caracter == '(': # Paréntesis de apertura
            pila.append(caracter)
        elif caracter == ')': # Paréntesis de cierre
            while pila and pila[-1] != '(':
                salida_postfija.append(pila.pop())
            if pila and pila[-1] == '(':
                pila.pop() # Sacar el '(' de la pila
        else: # Operador
            while (pila and pila[-1] != '(' and 
                   precedencia.get(caracter, 0) <= precedencia.get(pila[-1], 0)):
                salida_postfija.append(pila.pop())
            pila.append(caracter)
            
    # Sacar los operadores restantes pila
    while pila:
        salida_postfija.append(pila.pop())
        
    return "".join(salida_postfija)

if __name__ == "__main__":
    expresion_infija = input()
    expresion_postfija = convertFija(expresion_infija)
    print(expresion_postfija)