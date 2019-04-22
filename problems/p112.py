def bouncy(n):
    inc, dec = False, False
    d = n % 10
    n //= 10
    while n:
        if n % 10 < d:
            inc = True
        elif n % 10 > d:
            dec = True
        if inc and dec:
            return True
        d = n % 10
        n //= 10
    return False

c = 0
for n in range(1, 10**7):
    if bouncy(n):
        c += 1
    if c/n == 0.99:
        print(n)
