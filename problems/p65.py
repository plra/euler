cf_rep_e = [2]
for k in range(1, 100):
    cf_rep_e += [1, 2*k, 1]
cf_rep_sqrt_2 = [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,
                 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]


def conv(n, cf_rep):
    # start with "tail": 1/a_n
    num = 1
    denom = cf_rep[n-1]
    for i in range(n-2, -1, -1):
        a_i = cf_rep[i]
        # compute 1 / (a_i + num/denom)
        new_num = denom
        new_denom = a_i * denom + num
        num, denom = new_num, new_denom
    # numerator and denominator flipped at last step
    return (denom, num)


num, denom = conv(100, cf_rep_e)
print('{}/{} = {}'.format(num, denom, num/denom))
print(sum(int(d) for d in str(num)))
