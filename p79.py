pairs = set()
with open('res/keylog.txt') as f:
    for line in f:
        s = line.strip()
        x, y, z = list(map(int, list(s)))
        pairs.add((x, y))
        pairs.add((y, z))
print(pairs)

# u = (x, y), v = [v1, ..., vn]
def subpair(u, v):
    iu = 0
    for iv in range(len(v)):
        if v[iv] == u[iu]:
            iu += 1
        if iu == 2:
            return True
    return False

# return all possible minimal merges
def merge(u, v):
    x, y = u
    if subpair(u, v):
        return [v]
    if x in v and y in v:
        return [v + [y], [x] + v]
    if x in v:
        return [v + [y]]
    if y in v:
        return



print(subpair((1,2), [1,3,2,4]))
# print(min_code(codes))