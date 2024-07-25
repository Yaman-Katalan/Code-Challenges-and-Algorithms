# Write your test here
import pytest
from challenge03 import sum_of_unique_elements

def test_sum_of_unique_elements():
    # Test cases
    assert sum_of_unique_elements([1, 2, 3, 2]) == 4
    assert sum_of_unique_elements([1, 2, 3, 4, 5]) == 15
    assert sum_of_unique_elements([1, 1, 1, 1, 1]) == 0  # No unique elements
    assert sum_of_unique_elements([]) == 0  # Empty array
    assert sum_of_unique_elements([7, 8, 9, 8, 7]) == 9  # Only one unique element
    assert sum_of_unique_elements([1, 2, 2, 3, 3, 4, 5, 5]) == 5  # Multiple unique elements
    assert sum_of_unique_elements([10, 10, 10, 20, 30, 40, 40, 50]) == 100  # Mixed unique and non-unique elements

if __name__ == "__main__":
    pytest.main()
