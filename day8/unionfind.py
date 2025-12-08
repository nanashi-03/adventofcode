from collections import defaultdict

class UnionFind:
    def __init__(self):
        self.parents = dict()
        self.rank = defaultdict(lambda: 1)

    def _get_parent(self, point):
        if point not in self.parents:
            self.parents[point] = point
        return self.parents.get(point)

    def find(self, point):
        p = self._get_parent(point)
        while p != self._get_parent(p):
            p = self._get_parent(self._get_parent(p))
        return p

    def union(self, point1, point2):
        p1 = self.find(point1)
        p2 = self.find(point2)

        if p1 == p2:
            return self.rank[p2]

        if self.rank[p1] > self.rank[p2]:
            self.parents[p2] = p1
            self.rank[p1] += self.rank[p2]
            return self.rank[p1]
        else:
            self.parents[p1] = p2
            self.rank[p2] += self.rank[p1]
            return self.rank[p2]
