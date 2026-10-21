"""
Unit test suite for Exponential Search.
"""
from search.exponential_search import exponential_search

def test_exponential():
    arr = [2, 3, 4, 10, 40, 50, 80, 100]
    assert exponential_search(arr, 10) == 3
    assert exponential_search(arr, 99) == -1
