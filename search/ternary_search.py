"""
Ternary search algorithm for maximum/minimum of unimodal functions.
"""
def ternary_search(f, left: float, right: float, eps: float = 1e-9) -> float:
    while right - left > eps:
        m1 = left + (right - left) / 3
        m2 = right - (right - left) / 3
        if f(m1) < f(m2): left = m1
        else: right = m2
    return (left + right) / 2
