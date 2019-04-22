# a^b > b^c iff b log a > c log b
from math import log

bes = []
with open('res/base_exp.txt') as f:
    for line in f:
        b, e = line.strip().split(',')
        bes.append((int(b), int(e)))

max_log = 0
line_num = 0
for i in range(len(bes)):
    b, e = bes[i]
    if e * log(b) > max_log:
        max_log = e * log(b)
        line_num = i+1

print(line_num, max_log)