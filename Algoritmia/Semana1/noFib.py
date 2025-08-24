def resolverNoFibonacci():
    try:
        N = int(input())
    except (ValueError, IndexError):
        return

    fibSet = {1}
    a, b = 1, 1

    while b < N:
        fibSet.add(b)
        a, b = b, a + b

    numerosNoFib = []
    for i in range(1, N):
        if i not in fibSet:
            numerosNoFib.append(i)
            
    print(" ".join(map(str, numerosNoFib)))

if __name__ == "__main__":
    resolverNoFibonacci()