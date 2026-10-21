"""
Unit test suite for LFU cache.
"""
from structures.lfu_cache import LFUCache

def test_lfu():
    cache = LFUCache(2)
    cache.put(1, 1); cache.put(2, 2)
    assert cache.get(1) == 1
    cache.put(3, 3)
    assert cache.get(2) == -1
