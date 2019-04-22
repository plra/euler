import numpy as np
from queue import Queue
from collections import Counter

A = np.array([[1, -2, 2], [2, -1, 2], [2, -2, 3]])
B = np.array([[1, 2, 2], [2, 1, 2], [2, 2, 3]])
C = np.array([[-1, 2, 2], [-2, 1, 2], [-2, 2, 3]])


def get_primitive_triples(max_L):
    trips = []
    Ls = []
    q = Queue()
    q.put(np.array([3, 4, 5]))
    while not q.empty():
        t = q.get()
        L = np.sum(t)
        if L <= max_L:
            trips.append(t)
            Ls.append(L)
            q.put(A @ t)
            q.put(B @ t)
            q.put(C @ t)
    return trips, Ls


def has_one_triple(L, prim_Ls):
    k = 0
    for pL in prim_Ls:
        if L % pL == 0:
            k += 1
        if k > 1:
            return False
    return k == 1


max_L = 1500000
_, prim_Ls = get_primitive_triples(max_L)
print('{} primitive triples'.format(len(prim_Ls)))
prim_Ls.sort()
print('Sorted')

rts = Counter()
for L in prim_Ls:
    for L_p in range(L, max_L + 1, L):
        rts[L_p] += 1
print(sum(k == 1 for k in rts.values()))
# print(count_primitive_triples(100))
