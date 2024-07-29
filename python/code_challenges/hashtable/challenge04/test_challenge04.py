# Write your test here
import pytest
from challenge04 import sort_people

def test_sort_people():
    # Test case 1: Basic case with unique names and heights
    names = ["Alice", "Bob", "Charlie"]
    heights = [155, 185, 150]
    expected_output = ["Bob", "Alice", "Charlie"]
    assert sort_people(names, heights) == expected_output

    # Test case 2: Duplicate names with different heights
    names = ["Alice", "Bob", "Bob"]
    heights = [155, 185, 150]
    expected_output = ["Bob", "Alice", "Bob"]
    assert sort_people(names, heights) == expected_output

    # Test case 3: All names are the same
    names = ["Alice", "Alice", "Alice"]
    heights = [155, 185, 150]
    expected_output = ["Alice", "Alice", "Alice"]
    assert sort_people(names, heights) == expected_output

    # Test case 4: Already sorted in descending order
    names = ["Charlie", "Alice", "Bob"]
    heights = [200, 180, 160]
    expected_output = ["Charlie", "Alice", "Bob"]
    assert sort_people(names, heights) == expected_output

    # Test case 5: Empty input lists
    names = []
    heights = []
    expected_output = []
    assert sort_people(names, heights) == expected_output

    # Test case 6: Single element in the list
    names = ["Alice"]
    heights = [155]
    expected_output = ["Alice"]
    assert sort_people(names, heights) == expected_output

if __name__ == "__main__":
    pytest.main()
