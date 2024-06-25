# Write your test here
import pytest
from challenge01 import buildTree, TreeNode

def tree_equals(tree1, tree2):
    if not tree1 and not tree2:
        return True
    if not tree1 or not tree2:
        return False
    return (tree1.val == tree2.val and
            tree_equals(tree1.left, tree2.left) and
            tree_equals(tree1.right, tree2.right))

def test_example1():
    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]
    expected_tree = TreeNode(3)
    expected_tree.left = TreeNode(9)
    expected_tree.right = TreeNode(20)
    expected_tree.right.left = TreeNode(15)
    expected_tree.right.right = TreeNode(7)
    
    root = buildTree(preorder, inorder)
    assert tree_equals(root, expected_tree)

def test_example2():
    preorder = [-1]
    inorder = [-1]
    expected_tree = TreeNode(-1)
    
    root = buildTree(preorder, inorder)
    assert tree_equals(root, expected_tree)

def test_empty_tree():
    preorder = []
    inorder = []
    expected_tree = None
    
    root = buildTree(preorder, inorder)
    assert tree_equals(root, expected_tree)

def test_single_node():
    preorder = [1]
    inorder = [1]
    expected_tree = TreeNode(1)
    
    root = buildTree(preorder, inorder)
    assert tree_equals(root, expected_tree)

def test_full_left_subtree():
    preorder = [1, 2, 3, 4, 5]
    inorder = [5, 4, 3, 2, 1]
    expected_tree = TreeNode(1)
    expected_tree.left = TreeNode(2)
    expected_tree.left.left = TreeNode(3)
    expected_tree.left.left.left = TreeNode(4)
    expected_tree.left.left.left.left = TreeNode(5)
    
    root = buildTree(preorder, inorder)
    assert tree_equals(root, expected_tree)

def test_full_right_subtree():
    preorder = [1, 2, 3, 4, 5]
    inorder = [1, 2, 3, 4, 5]
    expected_tree = TreeNode(1)
    expected_tree.right = TreeNode(2)
    expected_tree.right.right = TreeNode(3)
    expected_tree.right.right.right = TreeNode(4)
    expected_tree.right.right.right.right = TreeNode(5)
    
    root = buildTree(preorder, inorder)
    assert tree_equals(root, expected_tree)

