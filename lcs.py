def LCS(X, Y):
    m = len(X)
    n = len(Y)
    LCS = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                LCS[i][j] = LCS[i - 1][j - 1] + 1
            else:
                LCS[i][j] = max(LCS[i - 1][j], LCS[i][j - 1])
    return LCS[m][n]

X = "ABCBDAB"
Y = "BDCABA"
print(LCS(X, Y))