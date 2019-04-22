from sympy import gcd

max_d = 12000

n_fracs = 0
# count 1/3 < n/d < 1/2
for d in range(2, max_d+1):
    n_min = int(d/3 + 1)
    n_max = int(d/2)
    if d % 2 == 0:
        n_rg = range(n_min | 1, n_max+1, 2)
    else:
        n_rg = range(n_min, n_max+1)
    for n in n_rg:
        if gcd(n, d) == 1:
            n_fracs += 1
    print('{}/{} - {}/{}: {} total'.format(n_min, d, n_max, d, n_fracs))

# counted 1/2...
print(n_fracs - 1)
