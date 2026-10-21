"""
Divide and Conquer algorithm for finding the closest pair of points in O(n log n).
"""
import math

def dist(p1, p2): return math.hypot(p1[0] - p2[0], p1[1] - p2[1])

def closest_pair(points: list) -> float:
    pts_x = sorted(points, key=lambda p: p[0])
    pts_y = sorted(points, key=lambda p: p[1])
    def _closest(px, py):
        n = len(px)
        if n <= 3:
            return min(dist(px[i], px[j]) for i in range(n) for j in range(i + 1, n))
        mid = n // 2; mid_x = px[mid][0]
        left_y = [p for p in py if p[0] <= mid_x]
        right_y = [p for p in py if p[0] > mid_x]
        d = min(_closest(px[:mid], left_y), _closest(px[mid:], right_y))
        strip = [p for p in py if abs(p[0] - mid_x) < d]
        for i in range(len(strip)):
            for j in range(i + 1, min(i + 8, len(strip))):
                d = min(d, dist(strip[i], strip[j]))
        return d
    return _closest(pts_x, pts_y) if len(points) >= 2 else 0.0
