# how many 2n^2 - 1 are prime for n in {1, ..., 50M}?
from sympy import isprime

max_n = 50 * 10**6
n_prime = 0
for n in range(1, max_n + 1):
    if isprime(2 * n**2 - 1):
        n_prime += 1
    if n % 10**4 == 0:
        print(n, n_prime)
print(n_prime)
