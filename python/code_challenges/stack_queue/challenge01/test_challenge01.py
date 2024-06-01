# Write your test here
from challenge01 import MyQueue
import pytest

@pytest.fixture
def queue():
    return MyQueue()

def test_empty_queue(queue):
    assert queue.empty() == True

def test_push_and_peek(queue):
    queue.push(1)
    queue.push(2)
    assert queue.peek() == 1

def test_push_and_pop(queue):
    queue.push(1)
    queue.push(2)
    assert queue.pop() == 1
    assert queue.pop() == 2

def test_push_and_pop_alternate(queue):
    queue.push(1)
    queue.push(2)
    assert queue.pop() == 1
    queue.push(3)
    assert queue.peek() == 2
    assert queue.pop() == 2
    assert queue.pop() == 3
    assert queue.empty() == True

def test_peek_on_empty_queue(queue):
    with pytest.raises(IndexError):
        queue.peek()

def test_pop_on_empty_queue(queue):
    with pytest.raises(IndexError):
        queue.pop()

