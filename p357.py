from sympy import divisors, isprime, nextprime
from math import sqrt

max_n = 10**8

# 1 works
c = 1
for n in range(2, max_n+1, 2):
    rn = sqrt(n)
    ds = divisors(n)
    for d in ds:
        if not isprime(d + n//d):
            break
        if d > rn:
            # print('{} is pg'.format(n))
            c += n
            break
    if n % 10**5 == 0:
        print(n, c)
print(c)
