# (a - 1)^n + (a + 1)^n = \sum_{k=0}^n (1 + (-1)^{n-k}) \binom n k a^k.
# For n even, this is 2(\binom n 0 a^0 + \binom n 2 a^2 + \dots + \binom n n a^n),
# which is 2 modulo a^2.
# For n odd, 2(\binom n 1 a^1 + \binom n 3 a^3 + \dots + \binom n n a^n),
# which is 2na modulo a^2.
# Hence r_max = max_{n odd} (2na % a^2) = a*max(2n % a)
# This is just a(a-1) if a is odd, or a(a-2) otherwise

print(sum(a * (a - 2 + (a % 2)) for a in range(3, 1001)))