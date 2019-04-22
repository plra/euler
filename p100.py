# minimal b with 2b(b-1) = n(n-1)
# solve poly 2b^2 - 2b - n(n-1) = 0
# b = (2 +- sqrt(4 + 8n(n-1))) / 4
# int iff sqrt(4 + 8n(n-1)) = 2sqrt(1 + 2n(n-1)) equiv 2 mod 4
# iff sqrt(1 + 2n(n-1)) equiv 1 mod 4
# list halfdisc = 1^2, 5^2, 9^2, ...
# when 2n^2 - 2n + 1 integer?

from math import sqrt

def P(b, n):
    return b * (b-1) / n / (n-1)

n = 1001880000000
n=2
while True:
    halfdisc = sqrt(1 + 2*n*(n-1))
    if halfdisc % 4 == 1.:
        b = (2 + 2*halfdisc) / 4
        # assert b==int(b)
        if 2*b*(b-1) == n*(n-1):
            print("FOUND {}, {}, {}".format(n, b, P(b, n)))
    elif n % 10**7 == 0:
        print(n)
    n += 1
