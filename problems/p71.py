max_d = 10**6
# 3/7 = 428571/999999

dists = []
for denom in range(1, max_d):
    if denom % 7 == 0:
        dists.append(2**64)
        continue
    num = int(3/7*denom)
    # print('{}/{}'.format(num, denom))
    dists.append(3/7 - num/denom)

min_d = 2**64
denoms = []
for denom, d in enumerate(dists):
    if d == min_d:
        denoms.append(denom)
    elif d < min_d:
        denoms = [denom]
        min_d = d

print(min_d, denoms)