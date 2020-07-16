import numpy as np


phi = (1 + np.sqrt(5)) / 2


def log10_F(n):
    return n * np.log10(phi) - np.log10(5) / 2


def first_digits(log10_x, n_digits):
    # If log10(x) = m + f, where m is an integer, find digits from 10^f
    f = log10_x - int(log10_x)
    return str(10**(f + n_digits - 1))[:n_digits]


def is_pandigital(n):
    digits = set(str(n))
    return len(digits) == 9 and '0' not in digits


last9_F = [1, 1]
for n in range(3, 10**6):
    last9_F_n = (last9_F[-1] + last9_F[-2]) % 10**9
    last9_F.append(last9_F_n)
    if is_pandigital(last9_F_n):
        log10_F_n = log10_F(n)
        first9_F_n = first_digits(log10_F_n, 9)
        if is_pandigital(first9_F_n):
            print(n, log10_F_n)
            break
