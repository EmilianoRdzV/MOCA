ops = {'+', '-', '*', '/', '^'}
prec = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}

def infixToPrefix(expr):
    stk = []
    out = []

    for ch in reversed(expr):
        if 'A' <= ch <= 'Z':
            out.append(ch)
        elif ch == ')':
            stk.append(ch)
        elif ch == '(':
            while stk and stk[-1] != ')':
                out.append(stk.pop())
            if stk:
                stk.pop()
        elif ch in ops:
            while stk and stk[-1] in ops and prec[stk[-1]] > prec[ch]:
                out.append(stk.pop())
            stk.append(ch)

    while stk:
        out.append(stk.pop())

    return "".join(reversed(out))

if __name__ == "__main__":
    expr = input()
    print(infixToPrefix(expr))
