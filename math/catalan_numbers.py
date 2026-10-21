"""
Catalan number sequence dynamic calculation for combinatorial structures.
"""
def catalan_number(n: int) -> int:
    if n <= 1: return 1
    c = [0] * (n + 1)
    c[0] = c[1] = 1
    for i in range(2, n + 1):
        for j in range(i):
            c[i] += c[j] * c[i - 1 - j]
    return c[n]
