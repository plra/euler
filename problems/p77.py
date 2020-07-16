from sympy import divisors, isprime, nextprime, sieve
from collections import defaultdict as ddict

max_n = 5
primes = list(sieve.primerange(0, max_n + 1))
ways = ddict(lambda: 0)
ways[2] = 1

done = False
while not done:
    done = True
    for p in primes:
        for n in ways.copy():
            if n + p <= max_n:
                ways[n+p] += 1
                done = False
