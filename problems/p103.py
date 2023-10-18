from itertools import combinations, product


# Get all disjoint subset pairs (B, C) of size (b, c) from A, which is given as a list.
# We require b <= c WOLOG.
def disjoint_subset_pairs(A):
    n = len(A)
    for b in range(1, n // 2 + 1):
        for B_indices in combinations(range(n), b):
            B = [A[i] for i in B_indices]
            remaining_indices = [i for i in range(n) if i not in B_indices]
            for c in range(1, n - b + 1):
                for C_indices in combinations(remaining_indices, c):
                    C = [A[i] for i in C_indices]
                    yield B, C


def is_special_set(A):
    # Short-circuits
    if len(A) >= 3 and A[0] + A[1] <= A[-1]:
        return False
    if len(A) >= 5 and A[0] + A[1] + A[2] <= A[-2] + A[-1]:
        return False
    for B, C in disjoint_subset_pairs(A):
        if sum(B) == sum(C):
            return False
        if len(C) > len(B) and sum(C) <= sum(B):
            return False
    return True


# Generates all increasing sequences with integer values in [a, c] of length l
def ascending_sequences(a, c, l):
    if l == 0:
        yield []
    for b in range(a, c + 1):
        for seq in ascending_sequences(b + 1, c, l - 1):
            yield [b] + seq


optimum_sets = [
    [1],
    [1, 2],
    [2, 3, 4],
    [3, 5, 6, 7],
    [6, 9, 11, 12, 13],
    [11, 18, 19, 20, 22, 25],
]
os_7_candidate = [20] + [20 + x for x in optimum_sets[5]]

if __name__ == "__main__":
    for A in ascending_sequences(19, 47, 7):
        if is_special_set(A):
            print(f"{A=}, {sum(A)=}")
