"""
Huffman entropy encoding for lossless text compression.
"""
import heapq
from collections import Counter

class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char; self.freq = freq; self.left = None; self.right = None
    def __lt__(self, other): return self.freq < other.freq

def build_huffman_codes(text: str) -> dict:
    if not text: return {}
    freq = Counter(text)
    pq = [HuffmanNode(ch, count) for ch, count in freq.items()]
    heapq.heapify(pq)
    while len(pq) > 1:
        n1 = heapq.heappop(pq); n2 = heapq.heappop(pq)
        merged = HuffmanNode(None, n1.freq + n2.freq)
        merged.left = n1; merged.right = n2
        heapq.heappush(pq, merged)
    root = pq[0]
    codes = {}
    def _traverse(node, prefix):
        if node.char is not None: codes[node.char] = prefix or "0"
        else:
            _traverse(node.left, prefix + "0")
            _traverse(node.right, prefix + "1")
    _traverse(root, "")
    return codes
