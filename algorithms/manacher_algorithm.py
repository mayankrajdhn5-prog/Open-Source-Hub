"""
Manacher linear time algorithm for longest palindromic substring discovery.
"""
def manacher(s: str) -> str:
    t = '#' + '#'.join(s) + '#'
    n = len(t)
    p = [0] * n
    c = r = 0
    for i in range(n):
        i_mirror = 2 * c - i
        if r > i: p[i] = min(r - i, p[i_mirror])
        while i + 1 + p[i] < n and i - 1 - p[i] >= 0 and t[i + 1 + p[i]] == t[i - 1 - p[i]]:
            p[i] += 1
        if i + p[i] > r:
            c = i; r = i + p[i]
    max_len, center = max((val, idx) for idx, val in enumerate(p))
    start = (center - max_len) // 2
    return s[start:start + max_len]
