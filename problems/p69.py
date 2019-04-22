# just look at phi(n)/n and reason that minimizer is smooth
from sympy import isprime, nextprime

def red(n, p):
    while n % p == 0:
        n /= p
    return n

def f(n, primes):
    v = 1
    n_r = n
    for p in primes:
        if p > n_r:
            break
        n_r = red(n_r, p)
        if n_r != n:
            v *= p/(p-1)
    return v

max_n = 10**4

primes = []
p = 1
while True:
    p = nextprime(p)
    if p <= max_n:
        primes.append(p)
    else:
        break

# T = [None for _ in range(max_n+1)]
# T[1] = 1
print([f(n, primes) for n in range(2, max_n)])