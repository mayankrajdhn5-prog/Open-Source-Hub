"""
Unit test suite for Skip List.
"""
from structures.skip_list import SkipList

def test_skip_list():
    sl = SkipList()
    sl.insert(10); sl.insert(20); sl.insert(5)
    assert sl.header.forward[0].val == 5
