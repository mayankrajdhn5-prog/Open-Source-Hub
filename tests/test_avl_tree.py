"""
Unit test suite for AVL self-balancing tree.
"""
from structures.avl_tree import AVLTree

def test_avl():
    tree = AVLTree()
    root = None
    for val in [10, 20, 30, 40, 50, 25]:
        root = tree.insert(root, val)
    assert tree.balance(root) in (-1, 0, 1)
