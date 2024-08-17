n = 7

F = [[0] * (n + 1) for i in range(2)]
F[0][1] = 1
F[1][1] = 1

for i in range(2, n + 1):
    F[0][i] = F[0][i - 1] + F[1][i - 1]
    F[1][i] = F[0][i - 1]

print(F[0][n] + F[1][n])
