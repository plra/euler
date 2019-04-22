#Find the smallest prime which, by replacing part of the number(not necessarily adjacent digits) with the same digit, is part of an eight prime value family.
#p > 56003. do not swap last digit

import sympy

def single_locs(p):
    return [(i,) for i in range(len(str(p)) - 1)]

# do not consider swaps in last digit
def pair_locs(p):
    s = str(p)
    locs = []
    for i in range(len(s) - 2):
        for j in range(i + 1, len(s) - 1):
            if s[i] == s[j]:
                locs.append((i, j))
    return locs

def triple_locs(p):
    s = str(p)
    locs = []
    for i in range(len(s) - 3):
        for j in range(i + 1, len(s) - 2):
            for k in range(j + 1, len(s) - 1):
                if s[i] == s[j] == s[k]:
                    locs.append((i, j, k))
    return locs

def hits(p, tup):
    n = 0
    p_digits = list(str(p))
    for digit in range(10):
        for loc in tup:
            p_digits[loc] = str(digit)
        q = int(''.join(p_digits))
        if sympy.isprime(q) and len(str(p)) == len(str(q)):
            n += 1
    return n

p = 10000000
p = 50000
for it in range(2**63):
    p = sympy.nextprime(p)
    for tup in single_locs(p) + pair_locs(p) + triple_locs(p):
        n = hits(p, tup)
        if n >= 8:
            print('p={}, loc={}, hits={}'.format(p, tup, n))
            break
