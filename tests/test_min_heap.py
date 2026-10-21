"""
Unit test suite for Min Heap priority queue.
"""
from structures.min_heap import MinHeap

def test_min_heap():
    h = MinHeap()
    for v in [5, 3, 8, 1, 2]: h.push(v)
    assert [h.pop() for _ in range(5)] == [1, 2, 3, 5, 8]
