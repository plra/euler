# Need 1777^^1855 (mod 10^8). 1777 is prime, 1855 = 5 * 7 * 53
# Euler's theorem: a^phi(10^8) = 1 (mod 10^8). So can reduce exponents mod phi(10^8)

from sympy.ntheory import totient

a = 1777
k = 1855
m = 10**8

def tetration(a, k, m):
    phi_m = totient(m)
    res = 1
    for j in range(1, k + 1):
        res = pow(a, res, m)
        print(f'{a}^^{j} = {res}')
    return res

print(tetration(1777, 1855, 10**8))