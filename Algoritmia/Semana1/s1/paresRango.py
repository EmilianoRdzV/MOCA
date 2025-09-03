valorN, valorM = map(int, input().split())

primerPar = valorN
if primerPar % 2 != 0:
    primerPar = primerPar + 1

for numeroPar in range(primerPar, valorM + 1, 2):
    print(numeroPar)