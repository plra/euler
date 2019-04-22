from sympy import gcd
from sympy.ntheory import totient


max_d = 10**6

n_fracs = 0
for n in range(2, max_d+1):
    n_fracs += totient(n)
    if n % 10**5 == 0:
        print(n, n_fracs)

print(n_fracs)
