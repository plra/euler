from math import sqrt


def cf_rep_sqrt(n):
    rn = sqrt(n)
    if rn % 1 == 0:
        return 0

    a = [int(rn)]
    # consider x / (rn - y)
    x = 1
    y = a[0]
    (x_0, y_0) = (x, y)
    # find a_1 from (sqrt n + a_0) / (n - a_0^2)
    for i in range(1, 2**64):
        a_i = int(x / (rn - y))
        # conjugate: x(rn + y) / (n - y^2)
        # write a_i + (x rn + xy - a_i(n - y^2)) / (n - y^2)
        assert((n - y**2) % x == 0)
        x = (n - y**2) / x
        # this is the new x!
        y = a_i * x - y
        a.append(a_i)
        if (x, y) == (x_0, y_0):
            return a
    raise Exception('Math is over')


def digs(cf_rep, d):
    a = cf_rep[1:] * (d // len(cf_rep[1:]))


for n in range(2, 14):
    cf = cf_rep_sqrt(n)
    digs = digs(cf, 100)
    print(n, cf, digs)
