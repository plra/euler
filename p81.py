M = []
with open('res/matrix.txt') as f:
    for line in f:
        M.append([int(n) for n in line.strip().split(',')])

def minsum(M):
    S = [[None for _ in range(80)] for _ in range(80)]
    S[79][79] = M[79][79]
    for i in range(78, -1, -1):
        S[i][79] = M[i][79] + S[i+1][79]
    for j in range(78, -1, -1):
        S[79][j] = M[79][j] + S[79][j+1]

    for i in range(78, -1, -1):
        for j in range(78, -1, -1):
            print(i, j)
            S[i][j] = M[i][j] + min(S[i][j+1], S[i+1][j])
    return S[0][0]

print(minsum(M))
