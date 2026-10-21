"""
Shoelace formula for calculating the area of any planar polygon.
"""
def polygon_area(vertices: list) -> float:
    n = len(vertices)
    if n < 3: return 0.0
    area = 0.0
    for i in range(n):
        j = (i + 1) % n
        area += vertices[i][0] * vertices[j][1]
        area -= vertices[j][0] * vertices[i][1]
    return abs(area) / 2.0
