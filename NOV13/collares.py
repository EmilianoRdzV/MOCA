def calcularSeg(n, m, collar):
    collarDoble = collar + collar
    sumaPref = [0] * (2 * n + 1)
    for i in range(2 * n):
        sumaPref[i + 1] = sumaPref[i] + collarDoble[i]
        
    valMax = [0] * (m + 1)
    for l in range(1, m + 1):
        maxL = 0
        for i in range(n):
            maxL = max(maxL, sumaPref[i + l] - sumaPref[i])
        valMax[l] = maxL
    return valMax

def calcularDP(m, k, valMax):
    dp = [[-1] * (m + 1) for _ in range(k + 1)]
    dp[0][0] = 0
    
    for l in range(1, m + 1):
        val = valMax[l]
        for i in range(k, 0, -1):
            for j in range(m, l - 1, -1):
                if dp[i - 1][j - l] != -1:
                    dp[i][j] = max(dp[i][j], dp[i - 1][j - l] + val)
    return dp

def resolver():
    n, m, k = map(int, input().split())
    collarUno = list(map(int, input().split()))
    collarDos = list(map(int, input().split()))
    
    valMaxUno = calcularSeg(n, m, collarUno)
    dpUno = calcularDP(m, k, valMaxUno)
    
    valMaxDos = calcularSeg(n, m, collarDos)
    dpDos = calcularDP(m, k, valMaxDos)
    
    maxTotal = 0
    
    for k1 in range(k + 1):
        for m1 in range(m + 1):
            if dpUno[k1][m1] == -1:
                continue
            for k2 in range(k - k1 + 1):
                m2 = m - m1
                if m2 >= 0 and dpDos[k2][m2] != -1:
                    maxTotal = max(maxTotal, dpUno[k1][m1] + dpDos[k2][m2])
                    
    print(maxTotal)

resolver()