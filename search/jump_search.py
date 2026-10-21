"""
Jump search algorithm with optimal block step size sqrt(n).
"""
import math

def jump_search(arr: list, target: int) -> int:
    n = len(arr)
    if n == 0: return -1
    step = int(math.sqrt(n))
    prev = 0
    while arr[min(step, n) - 1] < target:
        prev = step
        step += int(math.sqrt(n))
        if prev >= n: return -1
    while arr[prev] < target:
        prev += 1
        if prev == min(step, n): return -1
    return prev if arr[prev] == target else -1
