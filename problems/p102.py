from shapely.geometry import Point
from shapely.geometry.polygon import Polygon

origin = Point(0, 0)
n = 0
with open('res/triangles.txt') as f:
    for line in f:
        x1, y1, x2, y2, x3, y3 = map(int, line.strip().split(','))
        tri = Polygon([(x1, y1), (x2, y2), (x3, y3)])
        n += tri.contains(origin)

print(n)

with open('res/triangles.txt') as f:
    tris = [map(int, line.strip().split(',')) for line in f]
    print(sum(Polygon([(a, b), (c, d), (e, f)]).contains(Point(0, 0))
              for a, b, c, d, e, f in tris))
