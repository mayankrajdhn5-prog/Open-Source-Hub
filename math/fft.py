"""
Cooley-Tukey radix-2 Fast Fourier Transform (FFT) polynomial multiplication.
"""
import cmath

def fft(a: list, invert: bool = False) -> list:
    n = len(a)
    if n <= 1: return a
    even = fft(a[0::2], invert)
    odd = fft(a[1::2], invert)
    angle = -2 * cmath.pi / n if not invert else 2 * cmath.pi / n
    w = 1; wn = cmath.exp(1j * angle)
    y = [0] * n
    for k in range(n // 2):
        y[k] = even[k] + w * odd[k]
        y[k + n // 2] = even[k] - w * odd[k]
        if invert: y[k] /= 2; y[k + n // 2] /= 2
        w *= wn
    return y
