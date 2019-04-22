from math import factorial


def sumfac(n):
    s = 0
    while n:
        d = n % 10
        s += factorial(d)
        n //= 10
    return s


loopers = {145: 1, 169: 3, 363601: 3, 1454: 3,
           871: 2, 45361: 2, 872: 2, 45362: 2}


def non_rep_terms(n, targ):
    for t in range(targ):
        if n in loopers:
            return t + loopers[n]
        n = sumfac(n)
    return None


targ = 60
ct = 0
for n in range(1, 10**6 + 1):
    if non_rep_terms(n, targ) == targ:
        ct += 1
    if n % 10**4 == 0:
        print(n, ct)
print(ct)
