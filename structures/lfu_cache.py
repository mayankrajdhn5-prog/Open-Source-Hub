"""
Least Frequently Used (LFU) cache with O(1) operations.
"""
from collections import defaultdict, OrderedDict

class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.vals = {}
        self.counts = {}
        self.freq_map = defaultdict(OrderedDict)
        self.min_freq = 0
    def get(self, key: int) -> int:
        if key not in self.vals: return -1
        count = self.counts[key]
        self.counts[key] = count + 1
        del self.freq_map[count][key]
        if not self.freq_map[count] and self.min_freq == count:
            self.min_freq += 1
        self.freq_map[count + 1][key] = True
        return self.vals[key]
    def put(self, key: int, value: int) -> None:
        if self.capacity <= 0: return
        if key in self.vals:
            self.vals[key] = value
            self.get(key)
            return
        if len(self.vals) >= self.capacity:
            k, _ = self.freq_map[self.min_freq].popitem(last=False)
            del self.vals[k]; del self.counts[k]
        self.vals[key] = value
        self.counts[key] = 1
        self.min_freq = 1
        self.freq_map[1][key] = True
