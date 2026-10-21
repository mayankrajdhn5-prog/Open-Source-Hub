"""
Lockless bounded ring buffer for streaming byte channels.
"""
class RingBuffer:
    def __init__(self, size: int):
        self.size = size
        self.buffer = [None] * size
        self.w = 0
        self.r = 0
    def write(self, val) -> bool:
        if (self.w + 1) % self.size == self.r: return False
        self.buffer[self.w] = val
        self.w = (self.w + 1) % self.size
        return True
    def read(self):
        if self.r == self.w: return None
        val = self.buffer[self.r]
        self.r = (self.r + 1) % self.size
        return val
