from itertools import permutations

def sort(n):
    return tuple(sorted([int(x) for x in str(n)]))

n_perms = {}
for n in range(1, 50000):
    l = sort(n**3)
    if l in n_perms:
        n_perms[l] = (n_perms[l][0] + 1, n_perms[l][1] + [n])
        if n_perms[l][0] == 5:
            print(n_perms[l])
            break
    else:
        n_perms[l] = (1, [n])