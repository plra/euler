from sympy.ntheory import totient

def up_mod(a, b, k, m):
    # exponentiation
    if k == 1:
        return pow(a, b, m)
    # power tower
    if k == 2:
        phi = totient(m)
        x = 0
        for _ in range(b):
            x = pow(a, x, phi)
            print(f'x = {x} mod {phi}')
        return pow(a, x, m)
    # three arrows: a ^^ (a ^^ (... ^^ a)), b times
    if k == 3:


def A_mod(n, m):
    if n == 0: return 1
    if n == 1: return 3
    if n == 2: return 7
    return up_mod(2, n + 3, n - 2, m) - 3

print(up_mod(2, 5, 2, 101))
print(A_mod(4, 14**8))