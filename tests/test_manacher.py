"""
Unit test suite for Manacher longest palindrome search.
"""
from algorithms.manacher_algorithm import manacher

def test_manacher():
    assert manacher("babad") in ("bab", "aba")
    assert manacher("cbbd") == "bb"
    assert manacher("racecar") == "racecar"
