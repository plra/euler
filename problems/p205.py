import numpy as np
import random
import itertools
from tqdm import tqdm

sides_p = 4
nroll_p = 9
sides_c = 6
nroll_c = 6


def compute_pmf(sides, nroll):
    """
    As dict {x: p} where P(sum rolls = x) = p.
    """
    pmf = {}
    possible_rolls = range(1, sides + 1)
    for roll in itertools.product(possible_rolls, repeat=nroll):
        x = sum(roll)
        if x not in pmf:
            pmf[x] = 0
        pmf[x] += 1/sides**nroll
    return pmf


def combine_pmfs(pdf_X, pdf_Y, f):
    """
    Computes pmf of f(X, Y)
    """
    pmf = {}
    for x, px in pdf_X.items():
        for y, py in pdf_Y.items():
            fxy = f(x, y)
            if fxy not in pmf:
                pmf[fxy] = 0
            pmf[fxy] += px * py
    return pmf


pmf_p = compute_pmf(sides_p, nroll_p)
pmf_c = compute_pmf(sides_c, nroll_c)
pmf_pmc = combine_pmfs(pmf_p, pmf_c, lambda x, y: x - y)

print(sum(p for x, p in pmf_pmc.items() if x > 0))


def sim_slow(n_games, shard_size=10**6):
    # Underpowered Monte Carlo simulation
    shards = int(n_games / shard_size)
    wins_p = 0
    for i in tqdm(range(shards)):
        rolls_p = np.random.randint(1, sides_p, size=(shard_size, nroll_p))
        rolls_c = np.random.randint(1, sides_c, size=(shard_size, nroll_c))
        outcomes_p = np.sum(rolls_p, axis=1) > np.sum(rolls_c, axis=1)
        wins_p += np.sum(outcomes_p)
    return wins_p / (shard_size * shards)
