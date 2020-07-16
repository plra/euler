from sympy import primerange, sieve, factorint
from infinite import product
from math import log, sqrt

# Maximize p^a q^b <= N
def M(p, q, N):
    M = 0
    max_a = int(log(N) / log(p))
    for a in range(1, max_a + 1):
        b = int(log(N / p ** a) / log(q))
        if b == 0:
            continue
        m = p ** a * q ** b
        # print("{}^{} * {}^{} = {}".format(p, a, q, b, m))
        if m > M:
            M = m
    return M


def S(N):
    Ms = set()
    for p in sieve.primerange(1, sqrt(N) + 1):
        for q in sieve.primerange(p + 1, N / p + 1):
            Ms.add(M(p, q, N))

    return sum(Ms)


def S_2(N):
    Ms = set()
    prime_pairs = set()
    for m in range(N, N // 2 - 1, -1):
        factors = factorint(m)
        if len(factors) != 2:
            continue
        p, q = factors.keys()
        if (p, q) in prime_pairs:
            continue
        # print("M({}, {}, {}) = {}".format(p, q, N, m))
        Ms.add(m)
        prime_pairs.add((p, q))
    return sum(Ms)


print(S_2(10 ** 7))
