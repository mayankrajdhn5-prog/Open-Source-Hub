"""
Augmented tree for efficient interval overlapping queries.
"""
class IntervalNode:
    def __init__(self, low, high):
        self.low = low; self.high = high; self.max = high
        self.left = None; self.right = None

def insert_interval(root, low, high):
    if not root: return IntervalNode(low, high)
    if low < root.low: root.left = insert_interval(root.left, low, high)
    else: root.right = insert_interval(root.right, low, high)
    root.max = max(root.max, high)
    return root

def overlap_search(root, low, high):
    if not root: return None
    if root.low <= high and low <= root.high: return (root.low, root.high)
    if root.left and root.left.max >= low: return overlap_search(root.left, low, high)
    return overlap_search(root.right, low, high)
