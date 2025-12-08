from unionfind import UnionFind
import heapq
from math import dist

lines = []
with open("input", "r") as f:
    for line in f.readlines():
        lines.append(line.strip())

coordinates = []

for line in lines:
    coordinates.append(tuple(map(int, line.split(','))))

minheap = []
n = len(coordinates)

for i in range(n - 1):
    for j in range(i + 1, n):
        heapq.heappush(minheap, (dist(coordinates[i], coordinates[j]), coordinates[i], coordinates[j]))

uf = UnionFind()

while True:
    _, p1, p2 = heapq.heappop(minheap)
    if uf.union(p1, p2) == n:
        print(p1[0] * p2[0])
        break


