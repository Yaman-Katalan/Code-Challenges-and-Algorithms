class Queue:
    def __init__(self):
        """
        Initialize an empty queue.
        """
        self.queue = []
    
    def is_empty(self):
        """
        Check if the queue is empty.
        
        :return: True if the queue is empty, False otherwise.
        """
        return len(self.queue) == 0
    
    def enqueue(self, item):
        """
        Add an item to the end of the queue.
        
        :param item: The item to be added to the queue.
        """
        self.queue.append(item)
    
    def dequeue(self):
        """
        Remove and return the item at the front of the queue.
        
        :return: The item at the front of the queue.
        :raises IndexError: If the queue is empty.
        """
        if self.is_empty():
            raise IndexError("Dequeue from an empty queue")
        return self.queue.pop(0)
    
    def size(self):
        """
        Get the number of items in the queue.
        
        :return: The size of the queue.
        """
        return len(self.queue)
    
    def __str__(self):
        """
        Get a string representation of the queue.
        
        :return: A string representing the items in the queue.
        """
        return ' -> '.join(map(str, self.queue))

def reverse_queue(q):
    """
    Reverse the order of items in a queue.
    
    :param q: The queue to be reversed.
    :return: The reversed queue.
    """
    stack = []
    
    while not q.is_empty():
        stack.append(q.dequeue())
    
    while stack:
        q.enqueue(stack.pop())
    
    return q

# Example usage

q = Queue()
for i in [5, 4, 3, 2, 1]:
    q.enqueue(i)

print("Original Queue:")
print(q)

reversed_q = reverse_queue(q)

print("Reversed Queue:")
print(reversed_q)
