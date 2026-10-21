"""
Binary Min Heap priority queue implementation from scratch.
"""
class MinHeap:
    def __init__(self): self.heap = []
    def push(self, val):
        self.heap.append(val)
        self._sift_up(len(self.heap) - 1)
    def pop(self):
        if not self.heap: return None
        if len(self.heap) == 1: return self.heap.pop()
        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._sift_down(0)
        return root
    def _sift_up(self, idx):
        parent = (idx - 1) // 2
        while idx > 0 and self.heap[idx] < self.heap[parent]:
            self.heap[idx], self.heap[parent] = self.heap[parent], self.heap[idx]
            idx = parent; parent = (idx - 1) // 2
    def _sift_down(self, idx):
        n = len(self.heap)
        while 2 * idx + 1 < n:
            smallest = 2 * idx + 1
            right = smallest + 1
            if right < n and self.heap[right] < self.heap[smallest]:
                smallest = right
            if self.heap[idx] <= self.heap[smallest]: break
            self.heap[idx], self.heap[smallest] = self.heap[smallest], self.heap[idx]
            idx = smallest
