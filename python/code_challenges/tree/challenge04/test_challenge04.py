# Write your test here

import pytest
from challenge04 import TreeNode, insert_node, find_max_inorder, build_tree

def test_find_max_inorder():
    values = [1000, 500, 2000, 250, 600, 12000]
    root = build_tree(values)
    max_value = find_max_inorder(root)
    assert max_value == 12000

def test_empty_tree():
    root = build_tree([])
    max_value = find_max_inorder(root)
    assert max_value == float('-inf')

def test_single_node():
    values = [42]
    root = build_tree(values)
    max_value = find_max_inorder(root)
    assert max_value == 42

def test_left_skewed_tree():
    values = [10, 5, 3, 1]
    root = build_tree(values)
    max_value = find_max_inorder(root)
    assert max_value == 10

def test_right_skewed_tree():
    values = [1, 3, 5, 10]
    root = build_tree(values)
    max_value = find_max_inorder(root)
    assert max_value == 10

def test_all_negative_values():
    values = [-10, -20, -30, -40]
    root = build_tree(values)
    max_value = find_max_inorder(root)
    assert max_value == -10

def test_duplicate_values():
    values = [5, 3, 7, 3, 7, 8]
    root = build_tree(values)
    max_value = find_max_inorder(root)
    assert max_value == 8
