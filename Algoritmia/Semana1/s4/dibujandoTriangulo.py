n = int(input())

nFilas = (n + 1) // 2

for i in range(1, nFilas + 1):
    nArr = 2 * i - 1
    nEsp = (n - nArr) // 2
    print(' ' * nEsp + '@' * nArr)