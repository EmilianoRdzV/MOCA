def tokenize(expression_str):
    """
    Convierte la cadena de expresión en una lista de tokens (números y operadores/paréntesis).
    Los números pueden tener múltiples dígitos.
    """
    tokens = []
    i = 0
    n = len(expression_str)
    while i < n:
        char = expression_str[i]

        if char.isdigit():
            num_str = ""
            while i < n and expression_str[i].isdigit():
                num_str += expression_str[i]
                i += 1
            tokens.append(int(num_str))
            continue  # El índice 'i' ya se avanzó, continuar con el siguiente ciclo
        elif char in ['+', '-', '*', '/', '(', ')']:
            tokens.append(char)
            i += 1
        else:
            # Esto no debería ocurrir si la entrada es válida y sin espacios
            # print(f"Carácter inesperado: {char}")
            i += 1
    return tokens

def infix_to_postfix(tokens):
    """
    Convierte una lista de tokens en formato infijo a formato postfijo (RPN)
    usando el algoritmo Shunting-yard.
    """
    output_queue = []
    operator_stack = []
    # Precedencia de operadores: * y / tienen mayor precedencia que + y -
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2} 
    # Todos los operadores (+, -, *, /) son asociativos a la izquierda.

    for token in tokens:
        if isinstance(token, int):  # Si el token es un número
            output_queue.append(token)
        elif token == '(':
            operator_stack.append(token)
        elif token == ')':
            while operator_stack and operator_stack[-1] != '(':
                output_queue.append(operator_stack.pop())
            if operator_stack and operator_stack[-1] == '(':
                operator_stack.pop()  # Sacar el '(' de la pila
            # (Se asume que los paréntesis están balanceados por la naturaleza del problema)
        else:  # Si el token es un operador
            # Mientras haya un operador en la cima de la pila con mayor o igual precedencia
            # (ya que todos son L-R asociativos), sacarlo.
            while (operator_stack and 
                   operator_stack[-1] != '(' and
                   precedence.get(operator_stack[-1], 0) >= precedence.get(token, 0)):
                output_queue.append(operator_stack.pop())
            operator_stack.append(token)

    # Sacar cualquier operador restante de la pila
    while operator_stack:
        output_queue.append(operator_stack.pop())
        
    return output_queue

def evaluate_postfix(postfix_tokens):
    """
    Evalúa una expresión en formato postfijo (RPN).
    """
    operand_stack = []
    for token in postfix_tokens:
        if isinstance(token, int):  # Si el token es un número
            operand_stack.append(token)
        else:  # Si el token es un operador
            if len(operand_stack) < 2:
                raise ValueError("Expresión postfija inválida: insuficientes operandos para el operador.")
            val2 = operand_stack.pop()
            val1 = operand_stack.pop()

            if token == '+':
                operand_stack.append(val1 + val2)
            elif token == '-':
                operand_stack.append(val1 - val2)
            elif token == '*':
                operand_stack.append(val1 * val2)
            elif token == '/':
                # División entera. En Python, // es división entera que redondea hacia abajo.
                # Para resultados siempre positivos, es igual a truncar.
                if val2 == 0:
                    raise ZeroDivisionError("División por cero.")
                operand_stack.append(val1 // val2) 
    
    if len(operand_stack) == 1:
        return operand_stack[0]
    else:
        # Esto podría indicar una expresión postfija malformada
        # o un error en la conversión. Para este problema, asumimos validez.
        raise ValueError("La pila de operandos no terminó con un solo resultado.")


if __name__ == "__main__":
    expression_string = input()
    
    # Paso 1: Tokenizar la expresión
    tokens = tokenize(expression_string)
    
    # Paso 2: Convertir de infijo a postfijo
    postfix_expression = infix_to_postfix(tokens)
    
    # Paso 3: Evaluar la expresión postfija
    result = evaluate_postfix(postfix_expression)
    
    # La salida en los ejemplos es solo el número.
    print(result)