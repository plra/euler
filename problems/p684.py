from math import floor, ceil

M = 1000000007
n_fibs = 90

fibs = [0, 1]
for i in range(2, n_fibs + 1):
    fibs.append(fibs[-1] + fibs[-2])


def S_mod(k, M):
    D = n // 9
    sigma = (6 * (pow(10, D, M) - 1) - 9 * D) % M
    for r in range(2, (k - 1) % 9 + 3):
        sigma = (sigma + r * pow(10, D, M) - 1) % M
    return sigma


for k in [1, 9, 10, 18, 19, 20]:
    print("S({}) = {}".format(k, S_mod(k, M)))

assert S_mod(20, M) == 1074


ans = 0
for i, f_i in enumerate(fibs):
    if i <= 1:
        continue
    S_f_i_mod_M = S_mod(f_i, M)
    ans = (ans + S_f_i_mod_M) % M
    print(
        "f_{} = {}, S(f_i) = {} (mod M), sum = {} (mod M)".format(
            i, f_i, S_f_i_mod_M, ans
        )
    )

