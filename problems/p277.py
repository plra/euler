# a1 = r1 mod 3
# a2 = (x1 a1 + y1) / 3 = r2 mod 3
# -> (x1 a1 + y1) / 3 = 3k + r2
# -> x1 a1 + y1 = 9k + 3r2 = 3r2 mod 9
# -> x1 a1 = 3r2 - y1 mod 9
# -> a1 = mmi(x1, 9) (3r2 - y1) mod 9
# a3 = (x2 a2 + y2) / 3 = r3 mod 3
# -> a2 = mmi(x2, 9) (3r3 - y2) mod 9 = M mod 9
# -> (x1 a1 + y1) / 3 = M mod 9
# -> a1 = mmi(x1, 27) (3M - y1) mod 27
# ...
# aN = (xN-1 aN-1 + yN-1) / 3 = rN mod 3

# step 1
# a1 = 0 mod 3
# step 2
# a2 = 2 mod 3
# a1 = mmi(1, 9) (3*2 - 0) mod 9 = 6 mod 9
# step 3
# a3 = 0 mod 3
# a2 = mmi(2, 9) (3*0 +1) mod 9 = 5 mod 9
# a1 = mmi(1, 27) (3*5 - 0) mod 27 = 15 mod 27

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

prefix = "UDDDUdddDDUDDddDdDddDDUDDdUUDd"
# prefix = "DdDddUUdDDDdUDUUUdDdUUDDDUdDD"
# prefix = "DdDddUUdDD"
step_map = {'D': (0, 1, 0), 'U': (1, 4, 2), 'd': (2, 2, -1)}
a_mod_3, x, y = list(zip(*[step_map[step] for step in prefix]))

modulus = 3
residue = a_mod_3[-1]
for n in range(len(prefix) - 1)[::-1]:
    modulus *= 3
    residue = (modinv(x[n], modulus) * (3 * residue - y[n])) % modulus
    print(f'a_{n} = {residue} mod {modulus}')

while residue <= 10**15:
    residue += modulus

print(residue)
# for nm1, l in enumerate(prefix):
#     n = nm1 + 1
#     modulus = 3**n

#     if l == 'D':
#         a_n_mod_3, x_n, y_n = 0, 1, 0
#     elif l == 'U':
#         a_n_mod_3, x_n, y_n = 1, 4, 2
#     elif l == 'd':
#         a_n_mod_3, x_n, y_n = 2, 2, -1
