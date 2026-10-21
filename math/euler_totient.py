"""
Euler's Totient function phi(n) counting coprime integers.
"""
def euler_totient(n: int) -> int:
    result = n
    p = 2
    while p * p <= n:
        if n % p == 0:
            while n % p == 0: n //= p
            result -= result // p
        p += 1
    if n > 1: result -= result // n
    return result
