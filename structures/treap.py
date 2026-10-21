"""
Randomized Cartesian Treap combining BST and Binary Heap properties.
"""
import random

class TreapNode:
    def __init__(self, key):
        self.key = key
        self.priority = random.random()
        self.left = None
        self.right = None

def right_rotate(y):
    x = y.left; y.left = x.right; x.right = y; return x

def left_rotate(x):
    y = x.right; x.right = y.left; y.left = x; return y

def treap_insert(root, key):
    if not root: return TreapNode(key)
    if key <= root.key:
        root.left = treap_insert(root.left, key)
        if root.left.priority > root.priority: root = right_rotate(root)
    else:
        root.right = treap_insert(root.right, key)
        if root.right.priority > root.priority: root = left_rotate(root)
    return root
