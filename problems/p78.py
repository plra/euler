from functools import lru_cache as memoize


@memoize(maxsize=None)
def p_(n, g):
    if g == 0 or n < 0:
        return 0
    if n <= 1 or g == 1:
        return 1
    return p_(n - g, g) + p_(n, g - 1)


def g(k):
    return k * (3*k - 1) // 2


def ks():
    for mag in range(1, 2**64):
        yield mag
        yield -mag


@memoize(maxsize=None)
def p(n):
    if n == 0 or n == 1:
        return 1
    n_parts = 0
    for k in ks():
        if g(k) > n:
            break
        n_parts += (-1)**(k-1) * p(n - g(k))
    return int(n_parts)


@memoize(maxsize=None)
def p_mod(n, m):
    if n == 0 or n == 1:
        return 1
    n_parts = 0
    for k in ks():
        if g(k) > n:
            break
        n_parts = (n_parts + (-1)**(k-1) * p_mod(n - g(k), m)) % m
    return int(n_parts)


for n in range(2**64):
    if p_mod(n, 10**6) == 0:
        print(n)
