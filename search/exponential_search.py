"""
Exponential search algorithm for unbounded or sorted arrays.
"""
import bisect

def exponential_search(arr: list, target: int) -> int:
    if not arr: return -1
    if arr[0] == target: return 0
    i = 1
    while i < len(arr) and arr[i] <= target: i *= 2
    idx = bisect.bisect_left(arr, target, i // 2, min(i, len(arr)))
    return idx if idx < len(arr) and arr[idx] == target else -1
