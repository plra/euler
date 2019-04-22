from sympy import isprime, nextprime
from itertools import permutations

def compatible(ps):
    for i in range(len(ps)):
        for j in range(len(ps)):
            if i == j:
                continue
            if not isprime(int(str(ps[i]) + str(ps[j]))):
                return False
    return True

# assumes ps is compatible
def extensions(ps, qs):
    es = []
    for q in qs:
        if ps and q <= ps[-1]:
            continue
        add = True
        for p in ps:
            if q == p or not isprime(int(str(p) + str(q))) or not isprime(int(str(q) + str(p))):
                add = False
                break
        if add:
            es.append(q)
    return es

# exclude 2; will always fail under p ++ 2
N = 1500
primes = [3]
for i in range(N-1):
    primes.append(nextprime(primes[i]))

print('largest prime: {}'.format(primes[-1]))

sets = [[]]
for r in range(5):
    new_sets = []
    for s in sets:
        es = extensions(s, primes)
        for q in es:
            new_sets.append(s + [q])
    sets = new_sets
    print('after round {}: {} candidates'.format(r+1, len(sets)))

print(sets)
