from sympy import sieve
from time import time


# Number of occurrences of digit `d` in integer `n`
def n_occs(n, d):
    return sum(c == str(d) for c in str(n))


def S(n, d):
    max_occs = 0
    s = 0
    for p in sieve.primerange(10 ** (n - 1), 10**n):
        occs = n_occs(p, d)
        if occs > max_occs:
            max_occs = occs
            s = p
        elif occs == max_occs:
            s += p
    return s


for n in range(1, 10):
    start = time()
    print(sum(S(n, d) for d in range(10)))
    print(time() - start)
