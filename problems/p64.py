from math import sqrt


def cf_period(n):
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
            return i
    return 'WTF'


ps = [cf_period(n) for n in range(1, 10001)]
print(ps[:50])
print(len([p for p in ps if p % 2 == 1]))
