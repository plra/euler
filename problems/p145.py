def reversible(n):
    if n % 10 == 0:
        return False
    s = n + int(str(n)[::-1])
    while s:
        if s % 2 == 0:
            return False
        s = s // 10
    return True
