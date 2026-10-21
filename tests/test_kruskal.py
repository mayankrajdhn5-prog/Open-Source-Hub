"""
Unit test suite for Kruskal Minimum Spanning Tree.
"""
from algorithms.kruskal_mst import kruskal_mst

def test_kruskal():
    edges = [(0, 1, 10), (0, 2, 6), (0, 3, 5), (1, 3, 15), (2, 3, 4)]
    mst = kruskal_mst(4, edges)
    total = sum(w for _, _, w in mst)
    assert total == 19
