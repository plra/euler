import numpy as np
from queue import PriorityQueue

M = []
with open('res/matrix2.txt') as f:
    for line in f:
        M.append([int(n) for n in line.strip().split(',')])

# M = [[131, 673, 234, 103, 18], [201, 96, 342, 965, 150], [
#     630, 803, 746, 422, 111], [537, 699, 497, 121, 956], [805, 732, 524, 37, 331]]
M = np.array(M)
n = M.shape[0]
visited = np.zeros(M.shape).astype(bool)


def neighbors(pos):
    r, c = pos
    nbrs = []
    if r < n - 1:
        nbrs.append((r + 1, c))
    if c < n - 1:
        nbrs.append((r, c + 1))
    return nbrs


pq = PriorityQueue()
start = (0, 0)
pq.put((start, M[start]))
visited[start] = True
while True:
    pos, partial_sum = pq.get()
    nbrs = neighbors(pos)
    if len(nbrs) == 0:
        print(partial_sum)
        break
    for nbr_pos in nbrs:
        if not visited[nbr_pos]:
            pq.put((nbr_pos, partial_sum + M[nbr_pos]))
            # visited[nbr_pos] = True
