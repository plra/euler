# Same as p108. We want n such that n^2 has lots of divisors: d(n^2) >= 8M.
# d(p_i^a_i ... p_r^a_r) = prod_i (a_i + 1).
# Thus d(n^2) = prod_i (2a_i + 1).
# So for squarefree n = p_i ... p_r, d(n^2) = 3^r.
# Then r >= log_3 8M = 14.5.
# So minimal squarefree n is p_1 ... p_15, but 3^15 = 14M.
# We need to minimize p_1^a_1 ... p_r^a_r : (2a_1 + 1) ... (2a_r + 1) >= 8M.
# I.e. minimize a_1 log p_1 + ... + a_r log p_r.

from sympy import sieve
from sympy.ntheory import divisor_count

n = 1
r = 0
for p in sieve.primerange(1, 40):
    n *= p
    r += 1
    print(f'r = {r}: p = {p}, n = {n}, s = {3**r}')

for k in range(1, 10**5):
    # Product of first several primes
    n = k * 7420738134810
    d = divisor_count(n**2)
    if d >= 8e6:
        print(f'n = {n}, d(n^2) = {d}')