from sympy import divisors, isprime, nextprime, sieve
from collections import defaultdict

primes = list(sieve.primerange(0, 10**2))
ways = {}
q = 2
for p in primes:
    if p - q == 2:
        # p is a twin prime
        ways[p] = 2
    else:
        ways[p] = 1
    q = p

# l = list(ways.items())
# for i in range(len(l)):
#     p, w_p = l[i]
#     for j in range(i, len(l)):
#         q, w_q = l[j]
#         if p + q not in ways:
#             ways[p + q] = w_p * w_q

def count(n):
    if n in ways:
        return ways[n]
    w = 0
    for p in primes:
        print(p)
        if p > n/2:
            return w
        if n - p in ways:
            print('{} = {} + {}'.format(n, n-p, p))
            w += ways[n - p] * ways[p]


for n in range(2, 10**2):
    ways[n] = count(n)

print(ways)