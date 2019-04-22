M = []
with open('res/matrix2.txt') as f:
    for line in f:
        M.append([int(n) for n in line.strip().split(',')])

# build map {(start_pos, end_pos): minsum}
def minsum(M, start_row, end_row):
    n = len(M)
    S = [[None for _ in range(n)] for _ in range(n)]

print(minsum(M, 0, 79))