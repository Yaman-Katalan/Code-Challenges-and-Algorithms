import pytest
from challenge01 import find_target, TreeNode  # Replace 'your_module' with the name of your module file

def create_bst_from_list(values):
    if not values:
        return None

    root = TreeNode(values[0])
    nodes = [root]
    index = 1

    for node in nodes:
        if index < len(values) and values[index] is not None:
            node.left = TreeNode(values[index])
            nodes.append(node.left)
        index += 1
        if index < len(values) and values[index] is not None:
            node.right = TreeNode(values[index])
            nodes.append(node.right)
        index += 1

    return root

def test_find_target_valid():
    root = create_bst_from_list([7, 2, 9, 1, 5, None, 14])
    assert find_target(root, 3) == True  # 2 + 1 = 3
    assert find_target(root, 6) == True  # 1 + 5 = 6
    assert find_target(root, 16) == True  # 7 + 9 = 16
    assert find_target(root, 21) == True  # 7 + 14 = 21

def test_find_target_invalid():
    root = create_bst_from_list([7, 2, 9, 1, 5, None, 14])
    assert find_target(root, 10) == True  # No pair sums to 10
    assert find_target(root, 20) == False  # No pair sums to 20


def test_find_target_empty_tree():
    root = create_bst_from_list([])
    assert find_target(root, 5) == False  # Empty tree, no pairs

def test_find_target_single_node():
    root = create_bst_from_list([5])
    assert find_target(root, 10) == False  # Only one node, no pairs
    assert find_target(root, 5) == False   # Only one node, no pair summing to 5
