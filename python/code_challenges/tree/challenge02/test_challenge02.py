# Write your test here
import pytest
from challenge02 import TreeNode, isSameTree  # Replace 'your_module_name' with the actual module name

def test_is_same_tree_true():
    # Tree 1: [1,2,3]
    p = TreeNode(1)
    p.left = TreeNode(2)
    p.right = TreeNode(3)

    # Tree 2: [1,2,3]
    q = TreeNode(1)
    q.left = TreeNode(2)
    q.right = TreeNode(3)

    assert isSameTree(p, q) == True

def test_is_same_tree_false_structure():
    # Tree 1: [1,2]
    p = TreeNode(1)
    p.left = TreeNode(2)

    # Tree 2: [1,null,2]
    q = TreeNode(1)
    q.right = TreeNode(2)

    assert isSameTree(p, q) == False

def test_is_same_tree_false_values():
    # Tree 1: [1,2,1]
    p = TreeNode(1)
    p.left = TreeNode(2)
    p.right = TreeNode(1)

    # Tree 2: [1,1,2]
    q = TreeNode(1)
    q.left = TreeNode(1)
    q.right = TreeNode(2)

    assert isSameTree(p, q) == False

def test_is_same_tree_both_empty():
    # Tree 1: []
    p = None

    # Tree 2: []
    q = None

    assert isSameTree(p, q) == True

def test_is_same_tree_one_empty():
    # Tree 1: [1]
    p = TreeNode(1)

    # Tree 2: []
    q = None

    assert isSameTree(p, q) == False
