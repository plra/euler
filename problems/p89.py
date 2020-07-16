nums = []
with open('res/roman.txt') as f:
    for line in f:
        nums.append(line.strip())

# In order of precedence
replacements = [('DCCCC', 'CM'), ('CCCC', 'CD'), ('LXXXX', 'XC'),
                ('XXXX', 'XL'), ('VIIII', 'IX'), ('IIII', 'IV')]


def reduce(s):
    for a, b in replacements:
        s = s.replace(a, b)
    return s


print(sum(len(s) for s in nums) - sum(len(reduce(s)) for s in nums))
