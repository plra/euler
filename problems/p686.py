from math import floor, ceil, log2


def first_digits(j):
    num_digits = ceil(j / log2(10))
    d_1 = floor(2 ** (j - (num_digits - 1) * log2(10)))
    d_2 = floor(2 ** (j - (num_digits - 2) * log2(10)) - 10 * d_1)
    d_3 = floor(2 ** (j - (num_digits - 3) * log2(10)) - 100 * d_1 - 10 * d_2)
    return [d_1, d_2, d_3][:num_digits]


for j in [1, 6, 7, 10, 16, 20, 80]:
    print(2 ** j, first_digits(j))


def p(L, n):
    num_finds = 0
    for j in range(1, 2 ** 64):
        if first_digits(j)[: len(L)] == L:
            num_finds += 1
            if num_finds % 10000 == 0:
                print("Found {}".format(num_finds))
            if num_finds == n:
                return j


big_n = 678910
assert p([1, 2], 1) == 7
assert p([1, 2], 2) == 80
assert p([1, 2, 3], 45) == 12710

# Alt solution
# Need 123 * 10^k <= 2^j <= 124 * 10^k for some k, i.e.
# lg 123 + x lg 10 <= j <= lg 124 + x lg 10
def p(L, n):
    num_finds = 0
    for x in range(2 ** 64):
        l = log2(L) + x * log2(10)
        r = log2(L + 1) + x * log2(10)
        if floor(l) != floor(r):
            # found solution j = floor(r)
            num_finds += 1
            if num_finds == n:
                return floor(r)


assert p(12, 1) == 7
assert p(12, 2) == 80
assert p(123, 45) == 12710
print(p(123, 678910))
