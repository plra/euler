import numpy as np

# empirical attempt
balls = []
for c in range(1, 8):
    balls += [c for _ in range(10)]
print(balls)

E = 0
for n in range(1, 10**6):
    pick = np.random.permutation(balls)[:20]
    u = len(np.unique(pick))
    E_p = E + (u - E) / n
    if round(E_p, 10) == round(E, 10):
        print(E_p, E)
        break

    E += (u - E) / n
    if n % 10**5 == 0:
        print(E)
