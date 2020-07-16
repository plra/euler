# Sequence x_n = an (mod p)
a = 1504170715041707
p = 4503599627370517

ecs = []
for n in range(1, 2 ** 64):
    x_n = (a * n) % p
    if len(ecs) == 0 or x_n < ecs[-1]:
        print("New EC: {}".format(x_n))
        ecs.append(x_n)
