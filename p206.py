# Find the unique positive integer whose square has the form 1_2_3_4_5_6_7_8_9_0
# 9 or 10 digits
from math import sqrt

min_n = int(sqrt(1020304050607080900)) // 10 * 10
max_n = sqrt(1929394959697989990)


def works(n):
    s = str(n**2)
    return s[2] == '2' and s[4] == '3' and s[6] == '4' and s[8] == '5' and s[10] == '6' and s[12] == '7' and s[14] == '8' and s[16] == '9' and s[18] == '0'
    return s[::2] == '1234567890'


for n in range(min_n, max_n, 10):
    if works(n):
        print(n, n**2)
        break
    if n % 10**6 == 0:
        print(n)
