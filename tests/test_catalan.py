"""
Unit test suite for Catalan numbers.
"""
from math.catalan_numbers import catalan_number

def test_catalan():
    assert [catalan_number(i) for i in range(6)] == [1, 1, 2, 5, 14, 42]
