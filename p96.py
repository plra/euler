grids = []
with open('res/sudoku.txt') as f:
    for _ in range(50):
        f.readline()
        grid = []
        for _ in range(9):
            grid.append([int(x) for x in f.readline().strip()])
        grids.append(grid)

def possible_vals(i, j, grid):
    vals = set(range(1, 10))
    for jp in range(9):
        if grid[i][jp] != 0:
            vals.discard(grid[i][jp])
    for ip in range(9):
        if grid[ip][j] != 0:
            vals.discard(grid[ip][j])
    box_i, box_j = i // 3, j // 3
    for ip in range(3*box_i, 3*box_i + 3):
        for jp in range(3*box_j, 3*box_j + 3):
            if (ip, jp) != (i, j) and grid[ip][jp] != 0:
                vals.discard(grid[ip][jp])
    return vals

def solve(grid):
    opts = []
    for i in range(9):
        for j in range(9):
            if grid[i][j] != 0:
                continue
            pvs = possible_vals(i, j, grid)
            opts.append((i, j, pvs))
    if not opts:
        return grid
    (i, j, pvs) = min(opts, key=lambda t: len(t[2]))
    if not pvs:
        return None
    grid_p = grid.copy()
    for pv in pvs:
        grid_p[i][j] = pv
        for ip in range(9):
            for jp in range(9):
                if not possible_vals(ip, jp, grid):
                    raise Exception
        soln = solve(grid_p)
        if soln:
            return soln
    return None


def next_cell(grid, i, j):
    for x in range(i, 9):
        for y in range(j, 9):
            if grid[x][y] == 0:
                return x, y
    for x in range(0, 9):
        for y in range(0, 9):
            if grid[x][y] == 0:
                return x, y
    return -1, -1


def is_valid(grid, i, j, e):
    rowOk = all([e != grid[i][x] for x in range(9)])
    if not rowOk:
        return False
    columnOk = all([e != grid[x][j] for x in range(9)])
    if not columnOk:
        return False
    secTopX, secTopY = 3 * (i//3), 3 * (j//3)
    for x in range(secTopX, secTopX+3):
        for y in range(secTopY, secTopY+3):
            if grid[x][y] == e:
                return False
    return True

def solve(grid, i=0, j=0):
    i, j = next_cell(grid, i, j)
    if i == -1:
        return grid
    for e in range(1, 10):
        if is_valid(grid, i, j, e):
            grid[i][j] = e
            soln = solve(grid, i, j)
            if soln:
                return soln
            # Undo the current cell for backtracking
            grid[i][j] = 0
    return None


solns = [solve(grid) for grid in grids]
print(solns)
print(sum([s[0][0] * 100 + s[0][1] * 10 + s[0][2] for s in solns]))