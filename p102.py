tris = []
with open('res/triangles.txt') as f:
    for line in f:
        tris.append([int(s) for s in line.strip().split(',')])

for x1, y1, x2, y2, x3, y3 in tris:
    print(x1)