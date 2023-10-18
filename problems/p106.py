# From property 2, we only need to check subsets of the same size m.
# Don't need to check m = 1 by construction.
#
# n = 4: From [a, b, c, d], only need to check a + d == b + c. In other pairs one subset "dominates"
# the other in the sense that its indices are lesser than the other subset's, i.e. we already know
# a + c < b + d since a < b and c < d.

from itertools import combinations


def n_subset_pairs_to_check(n):
    n_to_check = 0
    for m in range(2, n // 2 + 1):
        for A in combinations(range(n), m):
            for B in combinations((i for i in range(n) if i not in A), m):
                # A[0] < B[0] WOLOG
                if A[0] > B[0]:
                    continue
                if not all(A[i] < B[i] for i in range(m)):
                    n_to_check += 1
    return n_to_check


print(n_subset_pairs_to_check(12))
