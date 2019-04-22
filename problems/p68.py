# 10 must be external node
# rep as [[(o_1, i_1, j_1), ..., (o_5, i_5, j_5)]] with i_{k+1} = j_k
# independent params: o_k and i_k
from itertools import permutations


def solve():
    for assn in permutations(range(1, 11)):
        o = assn[:5]
        if 10 not in o:
            continue
        i = assn[5:]
        j = (i[1], i[2], i[3], i[4], i[0])
        s = o[0] + i[0] + j[0]
        if not all(o[k] + i[k] + j[k] == s for k in range(1, 5)):
            continue
        k_min, o_min = 0, 10
        for k in range(5):
            if o[k] < o_min:
                k_min, o_min = k, o[k]
        string = []
        for delta in range(5):
            k = (k_min + delta) % 5
            string.append((o[k], i[k], j[k]))
        print(string)


solve()
