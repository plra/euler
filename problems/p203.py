# binom(n, k) = n! / k! (n-k)!

from scipy.special import comb
from sympy.ntheory import factorint
from sympy import sieve

N_ROWS = 51
squarefree_bcs = {1}
for n in range(2, N_ROWS):
    for k in range(1, n // 2 + 1):
        bc = comb(n, k, exact=True)
        bc_fct = factorint(bc)
        if all(a < 2 for _, a in bc_fct.items()):
            print(f'{n} choose {k} = {bc} = {bc_fct}')
            squarefree_bcs.add(bc)

print(squarefree_bcs, sum(squarefree_bcs))