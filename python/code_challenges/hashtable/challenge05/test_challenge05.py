# Write your test here
import pytest
from challenge05 import arrays_intersection

def test_arrays_intersection_basic():
    arr1 = [1, 2, 2, 1]
    arr2 = [2, 2]
    assert sorted(arrays_intersection(arr1, arr2)) == [2]

def test_arrays_intersection_no_intersection():
    arr1 = [1, 2, 3]
    arr2 = [4, 5, 6]
    assert arrays_intersection(arr1, arr2) == []

def test_arrays_intersection_all_intersection():
    arr1 = [1, 2, 3]
    arr2 = [1, 2, 3]
    assert sorted(arrays_intersection(arr1, arr2)) == [1, 2, 3]

def test_arrays_intersection_mixed_intersection():
    arr1 = [4, 9, 5]
    arr2 = [9, 4, 9, 8, 4]
    assert sorted(arrays_intersection(arr1, arr2)) == [4, 9]

def test_arrays_intersection_empty_arr1():
    arr1 = []
    arr2 = [1, 2, 3]
    assert arrays_intersection(arr1, arr2) == []

def test_arrays_intersection_empty_arr2():
    arr1 = [1, 2, 3]
    arr2 = []
    assert arrays_intersection(arr1, arr2) == []

def test_arrays_intersection_both_empty():
    arr1 = []
    arr2 = []
    assert arrays_intersection(arr1, arr2) == []

def test_arrays_intersection_large_input():
    arr1 = list(range(1000))
    arr2 = list(range(500, 1500))
    expected = list(range(500, 1000))
    assert sorted(arrays_intersection(arr1, arr2)) == expected

if __name__ == "__main__":
    pytest.main()
