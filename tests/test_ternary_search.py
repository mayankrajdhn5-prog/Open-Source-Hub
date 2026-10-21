"""
Unit test suite for Ternary Search.
"""
from search.ternary_search import ternary_search

def test_ternary():
    # Peak at x = 3
    f = lambda x: -(x - 3) ** 2 + 10
    peak = ternary_search(f, 0, 10)
    assert abs(peak - 3.0) < 1e-4
