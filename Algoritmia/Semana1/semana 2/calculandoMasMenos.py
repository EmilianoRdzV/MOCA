a, b, c = map(float, input().split())

if b == 0:
    print("indefinido")
else:
    res1 = (a / b) + c
    res2 = (a / b) - c

    if res1 == res2:
        print(f"{res1:.6f}")
    else:
        print(f"{res1:.6f} {res2:.6f}")