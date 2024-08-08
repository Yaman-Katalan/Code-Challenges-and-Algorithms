import pytest
from challenge03 import sum_of_unique_elements

def test_sum_of_unique_elements_empty():
    assert sum_of_unique_elements([]) == 0

def test_sum_of_unique_elements_all_unique():
    assert sum_of_unique_elements([1, 2, 3, 4, 5]) == 15

def test_sum_of_unique_elements_no_unique():
    assert sum_of_unique_elements([1, 1, 2, 2, 3, 3]) == 0

def test_sum_of_unique_elements_some_unique():
    assert sum_of_unique_elements([1, 2, 2, 3, 4, 4, 5]) == 9

def test_sum_of_unique_elements_single_element():
    assert sum_of_unique_elements([42]) == 42

def test_sum_of_unique_elements_duplicates():
    assert sum_of_unique_elements([7, 7, 7, 7, 7]) == 0

def test_sum_of_unique_elements_mixed():
    assert sum_of_unique_elements([1, 2, 3, 1, 2, 3, 4]) == 4

def test_sum_of_unique_elements_negative_numbers():
    assert sum_of_unique_elements([-1, -2, -3, -1, -2, -4]) == -7

def test_sum_of_unique_elements_mixed_sign():
    assert sum_of_unique_elements([-1, 1, -2, 2, -3, 3, -1, 1, -2, 2]) == 0

def test_sum_of_unique_elements_zero_included():
    assert sum_of_unique_elements([0, 1, 2, 0, 3, 2]) == 4

# Running tests
if __name__ == "__main__":
    pytest.main()
