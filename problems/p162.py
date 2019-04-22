# 16-digit hex with 0, 1, A:
# 15 * 16^12 * (6 orders * 560 indices - 1 leading 0)

n = 0
for d in range(3, 17):
    n += 15*16**(d-1) + 41*14**(d-1) - (43*15**(d-1) + 13**d)

print(hex(n).upper())