# Write your test here
from challenge03 import Stack, delete_middle

def test_delete_middle_odd_elements():
    stack = Stack()
    for i in [1, 2, 3, 4, 5]:
        stack.push(i)
    stack = delete_middle(stack)
    assert str(stack) == str([1, 2, 4, 5])

def test_delete_middle_even_elements():
    stack = Stack()
    for i in [1, 2, 3, 4]:
        stack.push(i)
    stack = delete_middle(stack)
    assert str(stack) == str([1, 3, 4])

def test_delete_middle_single_element():
    stack = Stack()
    stack.push(1)
    stack = delete_middle(stack)
    assert str(stack) == str([])

def test_delete_middle_empty_stack():
    stack = Stack()
    stack = delete_middle(stack)
    assert str(stack) == str([])

def test_delete_middle_two_elements():
    stack = Stack()
    for i in [1, 2]:
        stack.push(i)
    stack = delete_middle(stack)
    assert str(stack) == str([2])

def test_delete_middle_large_stack():
    stack = Stack()
    for i in range(1, 11):  # Stack from 1 to 10
        stack.push(i)
    stack = delete_middle(stack)
    assert str(stack) == str([1, 2, 3, 4, 6, 7, 8, 9, 10])