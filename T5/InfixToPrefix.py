OPERATORS = {'+', '-', '*', '/', '^'}
PRECEDENCE = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}

ASSOCIATIVITY = {'^': 'R', '+': 'L', '-': 'L', '*': 'L', '/': 'L'}

def infix_to_postfix_for_prefix_conversion(expression):
    stack = []
    output = []

    for char in expression:
        if 'A' <= char <= 'Z':  # Operando
            output.append(char)
        elif char == '(':  # Paréntesis de apertura (originalmente era ')' )
            stack.append(char)
        elif char == ')':  # Paréntesis de cierre (originalmente era '(' )
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            if stack and stack[-1] == '(':
                stack.pop()  # Sacar el '(' de la pila
        elif char in OPERATORS:  # Operador
            while (stack and stack[-1] in OPERATORS and
                   (PRECEDENCE[stack[-1]] > PRECEDENCE[char] or
                    (PRECEDENCE[stack[-1]] == PRECEDENCE[char] and ASSOCIATIVITY[char] == 'R'))): # <--- CAMBIO CLAVE: 'L' a 'R'
                output.append(stack.pop())
            stack.append(char)

    while stack:
        output.append(stack.pop())

    return "".join(output)

def infix_to_prefix(expression):
    # Paso 1: Invertir la expresión infija
    reversed_expression = expression[::-1]

    # Paso 2: Intercambiar paréntesis en la expresión invertida
    swapped_parentheses_expression_list = []
    for char in reversed_expression:
        if char == '(':
            swapped_parentheses_expression_list.append(')')
        elif char == ')':
            swapped_parentheses_expression_list.append('(')
        else:
            swapped_parentheses_expression_list.append(char)
    processed_expression_for_postfix = "".join(swapped_parentheses_expression_list)

    # Paso 3: Convertir la expresión procesada a formato postfijo (usando la lógica ajustada)
    postfix_expression = infix_to_postfix_for_prefix_conversion(processed_expression_for_postfix)

    # Paso 4: Invertir la expresión postfija para obtener la prefija
    prefix_expression = postfix_expression[::-1]

    return prefix_expression

if __name__ == "__main__":
    infix_expression = input()
    if infix_expression:
        prefix_result = infix_to_prefix(infix_expression)
        print(prefix_result)
