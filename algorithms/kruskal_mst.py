"""
Kruskal algorithm for finding Minimum Spanning Tree using Disjoint Set Union.
"""
class UnionFind:
    def __init__(self, n: int):
        self.p = list(range(n))
    def find(self, x):
        if self.p[x] != x: self.p[x] = self.find(self.p[x])
        return self.p[x]
    def union(self, x, y):
        rx, ry = self.find(x), self.find(y)
        if rx != ry: self.p[rx] = ry; return True
        return False

def kruskal_mst(n: int, edges: list) -> list:
    edges.sort(key=lambda e: e[2])
    uf = UnionFind(n)
    mst = []
    for u, v, w in edges:
        if uf.union(u, v):
            mst.append((u, v, w))
            if len(mst) == n - 1: break
    return mst
