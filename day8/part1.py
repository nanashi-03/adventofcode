import heapq
from math import dist
from unionfind import UnionFind

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

for i in range(1000):
    _, p1, p2 = heapq.heappop(minheap)
    uf.union(p1, p2)

circuit_sizes = []
for parent in set(uf.parents.values()):
    circuit_sizes.append(uf.rank[parent] * -1)

heapq.heapify(circuit_sizes)

res = 1

for i in range(3):
    res = res * (heapq.heappop(circuit_sizes) * -1)

print(res)
