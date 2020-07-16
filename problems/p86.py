from itertools import combinations_with_replacement
from math import sqrt
from functools import lru_cache
import numpy as np


def n_iterative(M):
    n_cuboids_with_integer_shortest_route = 0
    for a, b, c in combinations_with_replacement(range(1, M + 1), 3):
        r = shortest_route(a, b, c)
        if r == int(r):
            n_cuboids_with_integer_shortest_route += 1
    return n_cuboids_with_integer_shortest_route


def shortest_route(a, b, c):
    # Assumes a <= b <= c
    return sqrt((a + b)**2 + c**2)


@lru_cache(maxsize=None)
def n(M):
    """
    Compute number of unique cuboids of side length <= M with integer opposite-corner shortest path
    """
    if M == 0:
        return 0
    # Either a cuboid has all sides <= M-1 or one of length M
    n_cuboids_with_integer_shortest_route = n(M - 1)
    for a in range(1, M + 1):
        for b in range(a, M + 1):
            r = shortest_route(a, b, M)
            if r == int(r):
                n_cuboids_with_integer_shortest_route += 1
    return n_cuboids_with_integer_shortest_route


n_cuboids_with_integer_shortest_route = 0
for a in range(1, 2**64):
    for b in range(1, a + 1):
        for c in range(1, b + 1):
            r = shortest_route(c, b, a)
            if r == int(r):
                n_cuboids_with_integer_shortest_route += 1
    if n_cuboids_with_integer_shortest_route > 10**5:
        print(a, n_cuboids_with_integer_shortest_route)
        break
