from sympy import sieve
from sympy.ntheory.generate import prevprime

MAX_N = 10**6

primes = sieve.primerange(1, MAX_N // 2 + 1)
n_leq = {}
for nm1, p in enumerate(primes):
    n_leq[p] = nm1 + 1

# print(n_leq)

n_semiprimes = 0
for p, n in n_leq.items():
    max_q = prevprime(MAX_N / p)
    if max_q > p:
        n_semiprimes += n_leq[max_q]
    # print(f'p={p}, max_q={max_q}, n={n_semiprimes}')

print(n_semiprimes)