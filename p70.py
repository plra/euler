from sympy.ntheory import factorint
from sympy import isprime
from math import sqrt

# max_n = 10**7
# T = [None for _ in range(max_n)]
# primes = sympy.sieve.primerange(2, max_n)


def phi_n_over_n(n):
    pfs = factorint(n)
    num, denom = 1, 1
    for p in pfs:
        num *= p - 1
        denom *= p
    return (num, denom)


def isperm(x, y):
    return sorted(str(x)) == sorted(str(y))


ub = 10**7


def naive_soln():
    best_n, best_f = 0, 2**64
    for n in range(6600001, ub + 1, 2):
        (num, denom) = phi_n_over_n(n)
        f = denom / num
        phi_n = int(n / denom * num)
        if isperm(phi_n, n):
            print('phi({}) = {}'.format(n, phi_n))
            if f < best_f:
                best_n, best_f = n, f
        if n % 200000 == 1:
            print(best_n, best_f)

        return best_n, best_f
