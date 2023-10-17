# Clearly x, y > n, and WOLOG x >= y.
# Rearrange: n(x + y) = xy, or y = nx / (x - n).
# Write z = x - n. Then y = n(z + n) / z = n + n^2/z.
# Solution iff y is an integer iff z | n^2.
# Number of (x, y) solns is divisor count d(n^2) since y and z are free parameters.
# Number of unique solns is (d(n^2) + 1) / 2 (eliminate duplicates, keep (2n, 2n))

from sympy.ntheory import divisor_count

for n in range(1, 10**6):
    n_solns = (divisor_count(n**2) + 1) / 2
    # if n_solns > 100:
    #     print(f'n = {n}: {n_solns} solutions')
    if n_solns > 1000:
        print(f'n = {n}: {n_solns} solutions')
        break