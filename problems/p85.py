def n_rects(n, m):
    r = 0
    for h in range(1, n+1):
        for w in range(1, m+1):
            r += (n - h + 1) * (m - w + 1)
    return r

target = 2 * 10**6
best = (None, None, 2**63)
for n in range(1, 100):
    for m in range(n, 100):
        r = n_rects(n, m)
        if abs(target - r) < abs(target - best[2]):
            best = (n, m, r)

print(best)