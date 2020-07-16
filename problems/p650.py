from scipy.special import binom
from sympy import sieve
from sympy.ntheory import factorint
from sympy.ntheory.primetest import isprime
from collections import defaultdict as ddict
from itertools import chain


def merge_with(d1, d2, f):
    merged_keys = {**d1, **d2}.keys()
    return {k: f(d1.get(k) or 0, d2.get(k) or 0) for k in merged_keys}


def dict_add(d1, d2):
    return merge_with(d1, d2, lambda x, y: x + y)


def dict_sub(d1, d2):
    return merge_with(d1, d2, lambda x, y: x - y)


def dict_mul(d, x):
    return {k: v*x for k, v in d.items()}


def memoize_unary(f):
    """
    Decorator
    """
    class memodict(dict):
        def __missing__(self, key):
            ret = self[key] = f(key)
            return ret
    return memodict().__getitem__


@memoize_unary
def pf_factorial(n):
    if n <= 1:
        return {}
    return dict_add(factorint(n), pf_factorial(n-1))


@memoize_unary
def pf_B(n):
    """
    B(n) = B(n-1) n^n / n!,
    so the prime factorization of B(n) is pf(B(n-1)) + n*pf(n) - pf(n!), where operations are
    defined on dicts.
    """
    if n <= 1:
        return {}
    return dict_sub(dict_add(pf_B(n-1), dict_mul(factorint(n), n - 1)), pf_factorial(n - 1))


def D(n):
    """
    D(n) = \sum_{d | B(n)} d.
    Let B(n) = \prod_k p_k^{a_k}. Then
    D(n) = \prod_k \sum_{i=0}^{a_k} p_k^i
         = \prod_k (p_k^{a_k + 1} - 1) / (p_k - 1).

    Blows up in your face for large n
    """
    pfs = pf_B(n)
    d = 1
    for p_k, a_k in pfs.items():
        d *= (p_k**(a_k + 1) - 1) / (p_k - 1)
    return d


def S(n):
    return sum(D(k) for k in range(1, n+1))


def sum_mod(xs, m):
    s = 0
    for x in xs:
        s = (s + x) % m
    return s


def D_mod(n, m):
    pfs = pf_B(n)
    d = 1
    for p_k, a_k in pfs.items():
        term = (pow(p_k, a_k + 1, m) - 1) * pow(p_k - 1, m - 2, m)
        d = (d * term) % m
    return d


def S_mod(n, m, verbose=0):
    s = 0
    for k in range(1, n+1):
        d_k_mod_m = D_mod(k, m)
        s = (s + d_k_mod_m) % m
        if verbose > 0 and k % 1000 == 0:
            print('D({}) % m = {}; S({}) % m = {}'.format(k, d_k_mod_m, k, s))
    return s


m = 1000000007

# assert isprime(m)
# assert S(5) == 5736
# assert S(10) == 141740594713218418
# assert S_mod(100, m, verbose=1) == 332792866

print(S_mod(20000, m, verbose=0))
