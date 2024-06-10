# Write your test here
from challenge04 import Queue
import pytest

# Create an instance of Queue for testing
@pytest.fixture
def queue():
    q = Queue()
    for i in [1, 2, 3, 4, 5]:
        q.enqueue(i)
    return q

def test_queue_is_empty(queue):
    assert queue.is_empty() == False

def test_queue_enqueue(queue):
    queue.enqueue(6)
    assert queue.size() == 6

def test_queue_dequeue(queue):
    assert queue.dequeue() == 1
    assert queue.size() == 4

def test_reverse_queue(queue):
    def reverse_queue(q):
        stack = []
        while not q.is_empty():
            stack.append(q.dequeue())
        while stack:
            q.enqueue(stack.pop())
        return q
    
    reversed_q = reverse_queue(queue)
    assert reversed_q.dequeue() == 5
    assert reversed_q.dequeue() == 4
    assert reversed_q.dequeue() == 3
    assert reversed_q.dequeue() == 2
    assert reversed_q.dequeue() == 1
    assert reversed_q.is_empty() == True


