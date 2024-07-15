# Write your test here
import pytest
from challenge03 import TreeNode, sortedArrayToBST, printLevelOrder

def test_sortedArrayToBST():
    # Test Case 1: Input [0, -3, -10, 5, 9]
    nums1 = [0, -3, -10, 5, 9]
    expected_output1 = [0, -3, 9, -10, "null", 5]
    tree1 = sortedArrayToBST(nums1)
    actual_output1 = printLevelOrder(tree1)
    
    # Assert that all elements in expected_output1 are present in actual_output1
    for val in expected_output1:
        assert val in actual_output1

    # Optionally, you can assert that the lengths are the same
    assert len(actual_output1) == len(expected_output1)

    # Additional assertions based on your specific needs

if __name__ == "__main__":
    pytest.main()
