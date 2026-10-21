"""
Thread-safe cached memoization decorator utility.
"""
import threading
from functools import wraps

def thread_safe_memoize(func):
    cache = {}
    lock = threading.Lock()
    @wraps(func)
    def wrapper(*args):
        with lock:
            if args in cache: return cache[args]
        res = func(*args)
        with lock: cache[args] = res
        return res
    return wrapper
