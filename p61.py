def P3(n):
    return n * (n+1) // 2

def P4(n):
    return n**2

def P5(n):
    return n * (3*n - 1) // 2

def P6(n):
    return n * (2*n - 1)

def P7(n):
    return n * (5*n - 3) // 2

def P8(n):
    return n * (3*n - 2)

Ps = [P3, P4, P5, P6, P7, P8]
P_vals = []
for P in Ps:
    vs = []
    for n in range(2**64):
        m = P(n)
        if len(str(m)) == 4:
            vs.append(m)
        elif len(str(m)) > 4:
            break
    P_vals.append(vs)

def cycle(k, l):
    return str(k)[2:] == str(l)[:2]

# WOLOG say first value is a P3
# cand is (list, used_indices)
cands = [([k], [0]) for k in P_vals[0]]

def step(cands, P_vals):
    new_cands = []
    for (vals, used_idxs) in cands:
        for i in range(len(P_vals)):
            if i in used_idxs:
                continue
            for l in P_vals[i]:
                if cycle(vals[-1], l):
                    new_cands.append((vals + [l], used_idxs + [i]))
    return new_cands

for _ in range(5):
    cands = step(cands, P_vals)

print([vals for vals, _ in cands if cycle(vals[-1], vals[0])])
