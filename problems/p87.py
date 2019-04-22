from sympy import sieve
from itertools import product

N = 5 * 10**7
ps = list(sieve.primerange(0, 1 + int(pow(N, 1/2))))
qs = list(sieve.primerange(0, 1 + int(pow(N, 1/3))))
rs = list(sieve.primerange(0, 1 + int(pow(N, 1/4))))

expressible = set()
for p, q, r in product(ps, qs, rs):
    n = p**2 + q**3 + r**4
    if n < N:
        expressible.add(p**2 + q**3 + r**4)

print(len(expressible))