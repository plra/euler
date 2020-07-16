import numpy as np


def u(n):
    return 1 - n + n**2 - n**3 + n**4 - n**5 + n**6 - n**7 + n**8 - n**9 + n**10


U = np.array([u(n) for n in range(1, 20)])


def eval_poly(p, n):
    return np.sum(np.array(p) * np.power(n, np.arange(len(p))))


def op(a, d):
    """
    Find p(x) = b_0 + b_1 x + ... + b_d x^d for which p(1) = a_1, ..., p(d) = a_d.
    Spawns linear system Mb = a.
    """
    dim = d + 1
    a = a[:dim]
    M = np.tile(range(1, dim+1), (dim, 1)).T
    M = np.power(M, np.tile(range(dim), (dim, 1)))
    b = np.linalg.inv(M).dot(a)
    return np.rint(b)


sum_fits = 0
for d in range(11):
    p = op(U, d)
    print(d, p)
    for n in range(1, 11):
        op_d_n = eval_poly(p, n)
        if op_d_n != U[n-1]:
            print('FIT: p({}) = {} != {}'.format(n, op_d_n, U[n-1]))
            sum_fits += op_d_n
            break

print(sum_fits)
