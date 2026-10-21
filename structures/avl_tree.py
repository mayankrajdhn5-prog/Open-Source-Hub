"""
AVL self-balancing binary search tree implementation.
"""
class AVLNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def height(self, node): return node.height if node else 0
    def balance(self, node): return self.height(node.left) - self.height(node.right) if node else 0
    def right_rotate(self, y):
        x = y.left; t = x.right; x.right = y; y.left = t
        y.height = 1 + max(self.height(y.left), self.height(y.right))
        x.height = 1 + max(self.height(x.left), self.height(x.right))
        return x
    def left_rotate(self, x):
        y = x.right; t = y.left; y.left = x; x.right = t
        x.height = 1 + max(self.height(x.left), self.height(x.right))
        y.height = 1 + max(self.height(y.left), self.height(y.right))
        return y
    def insert(self, root, key):
        if not root: return AVLNode(key)
        if key < root.key: root.left = self.insert(root.left, key)
        else: root.right = self.insert(root.right, key)
        root.height = 1 + max(self.height(root.left), self.height(root.right))
        b = self.balance(root)
        if b > 1 and key < root.left.key: return self.right_rotate(root)
        if b < -1 and key > root.right.key: return self.left_rotate(root)
        if b > 1 and key > root.left.key:
            root.left = self.left_rotate(root.left); return self.right_rotate(root)
        if b < -1 and key < root.right.key:
            root.right = self.right_rotate(root.right); return self.left_rotate(root)
        return root
