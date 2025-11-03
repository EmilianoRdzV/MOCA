año = int(input())

if año % 400 == 0:
    print("ES BISIESTO")
elif año % 100 == 0:
    print("NO ES BISIESTO")
elif año % 4 == 0:
    print("ES BISIESTO")
else:
    print("NO ES BISIESTO")


