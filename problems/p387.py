from sympy import isprime
from sympy import nextprime


def sum_digits(n):
    r = 0
    while n:
        r, n = r + n % 10, n // 10
    return r


def is_harshad(n):
    return n % sum_digits(n) == 0


def is_rt_harshad(n):
    while n:
        if not is_harshad(n):
            return False
        n //= 10
    return True


def is_strong_harshad(n):
    if n == 0:
        return False
    sd = sum_digits(n)
    return n % sd == 0 and isprime(n // sd)


def is_strong_rt_harshad_prime(p):
    if not isprime(p):
        return False
    n = p // 10
    return is_strong_harshad(n) and is_rt_harshad(n)


# sum Harshad numbers with prefix and suffix_len-length suffix
# assumes prefix is nonzero, strong, right-truncatable Harshad
def sum_with_prefix(prefix, suffix_len):
    if suffix_len == 0:
        if is_strong_rt_harshad_prime(prefix):
            print('strong rt Harshad: {}'.format(prefix))
            return prefix
        else:
            return 0
    sigma = 0
    for next_dig in range(10):
        new_prefix = 10*prefix + next_dig
        if suffix_len == 1 or is_harshad(new_prefix):
            sigma += sum_with_prefix(new_prefix, suffix_len - 1)
    return sigma


# sum strong rt Harshad primes up to 10^d
def sum_up_to(d):
    sigma = 0
    for digits in range(2, d + 1):
        for first in range(1, 10):
            sigma += sum_with_prefix(first, digits - 1)
    return sigma


print(sum_up_to(14))
