"""
Unit test suite for Graham Scan 2D convex hull.
"""
from algorithms.graham_scan import convex_hull

def test_convex_hull():
    pts = [(0, 0), (1, 1), (2, 2), (2, 0), (0, 2), (1, 0.5)]
    hull = convex_hull(pts)
    assert len(hull) == 4
