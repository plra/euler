from random import randint
from collections import deque


def roll(sides=6, times=2):
    r = 0
    for _ in range(times):
        r += randint(1, sides)
    return r


class Space:
    def __init__(self, index, name):
        self.index = index
        self.name = name

    def __repr__(self):
        return "{}@{}".format(self.name, self.index)


class Board:
    def __init__(self, spaces):
        self.n = len(spaces)
        self.spaces = spaces
        self.names_by_index = {s.index: s.name for s in spaces}
        self.indices_by_name = {s.name: s.index for s in spaces}

    def from_list(space_names):
        return Board([Space(i, name) for i, name in enumerate(space_names)])

    def name(self, index):
        return self.spaces_by_index[index]

    def index(self, name):
        return self.indices_by_name[name]

    def space(self, i=None, nm=None):
        if i is not None:
            return self.spaces[i]
        if nm is not None:
            return self.spaces[self.index(nm)]

    def next_space_of_type(self, cur_space, prefix):
        for d in range(self.n):
            new_space = self.advance(cur_space, d)
            if new_space.name.startswith(prefix):
                return new_space

    def advance(self, cur_space, n):
        new_index = (cur_space.index + n) % self.n
        return self.space(new_index)


SPACES = list(
    [
        "GO",
        "A1",
        "CC1",
        "A2",
        "T1",
        "R1",
        "B1",
        "CH1",
        "B2",
        "B3",
        "JAIL",
        "C1",
        "U1",
        "C2",
        "C3",
        "R2",
        "D1",
        "CC2",
        "D2",
        "D3",
        "FP",
        "E1",
        "CH2",
        "E2",
        "E3",
        "R3",
        "F1",
        "F2",
        "U2",
        "F3",
        "G2J",
        "G1",
        "G2",
        "CC3",
        "G3",
        "R4",
        "CH3",
        "H1",
        "T2",
        "H2",
    ]
)


def take_turn(board, cs, prev_rolls):
    cur_roll = roll(6)
    prev_rolls.append(cur_roll)
    if all(r == cur_roll for r in prev_rolls):
        cs = board.space(nm="JAIL")
    else:
        cs = board.advance(cs, cur_roll)
        draw = randint(1, 16)
        if cs.name.startswith("CC"):
            if draw == 1:
                cs = board.space(nm="GO")
            elif draw == 2:
                cs = board.space(nm="JAIL")
        elif cs.name.startswith("CH"):
            if draw == 1:
                cs = board.space(nm="GO")
            elif draw == 2:
                cs = board.space(nm="JAIL")
            elif draw == 3:
                cs = board.space(nm="C1")
            elif draw == 4:
                cs = board.space(nm="E3")
            elif draw == 5:
                cs = board.space(nm="H2")
            elif draw == 6:
                cs = board.space(nm="R1")
            elif draw in [7, 8]:
                cs = board.next_space_of_type(cs, "R")
            elif draw == 9:
                cs = board.next_space_of_type(cs, "U")
            elif draw == 10:
                cs = board.advance(cs, -3)
    return cs, prev_rolls


N_TURNS = 10 ** 5
board = Board.from_list(SPACES)
counts = {s: 0 for s in board.spaces}

prev_rolls = deque(maxlen=3)
cs = board.space(i=0)
for _ in range(N_TURNS):
    counts[cs] += 1
    cs, prev_rolls = take_turn(board, cs, prev_rolls)
