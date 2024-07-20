import pytest

# Assuming the TreeNode, max_height, and build_tree functions are in the module named challenge05
from challenge05 import TreeNode, max_height, build_tree

def test_empty_tree():
    assert max_height(None) == 0

def test_single_node_tree():
    root = TreeNode(10)
    assert max_height(root) == 1

def test_left_skewed_tree():
    values = [10, 20, None, 30, None, None, None, 40]
    root = build_tree(values)
    assert max_height(root) == 3

def test_right_skewed_tree():
    values = [10, None, 20, None, 30, None, 40]
    root = build_tree(values)
    assert max_height(root) == 4

def test_balanced_tree():
    values = [10, 20, 30, 40, 28, 27, 50]
    root = build_tree(values)
    assert max_height(root) == 3

def test_given_example():
    values = [10, 20, 30, 40, 28, 27, 50, 29]
    root = build_tree(values)
    assert max_height(root) == 4

def test_complex_tree():
    values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, None, None, 14, 15]
    root = build_tree(values)
    assert max_height(root) == 4

# Helper function to build the tree from a list of values
def build_tree(values):
    if not values:
        return None
    
    root = TreeNode(values[0])
    queue = [root]
    index = 1
    
    while queue and index < len(values):
        node = queue.pop(0)
        
        if index < len(values) and values[index] is not None:
            node.left = TreeNode(values[index])
            queue.append(node.left)
        index += 1
        
        if index < len(values) and values[index] is not None:
            node.right = TreeNode(values[index])
            queue.append(node.right)
        index += 1
    
    return root
