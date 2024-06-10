class Queue:
    def __init__(self):
        self.queue = []
    
    def is_empty(self):
        return len(self.queue) == 0
    
    def enqueue(self, item):
        self.queue.append(item)
    
    def dequeue(self):
        if self.is_empty():
            raise IndexError("Dequeue from an empty queue")
        return self.queue.pop(0)
    
    def size(self):
        return len(self.queue)
    
    def __str__(self):
        return ' -> '.join(map(str, self.queue))

def reverse_queue(q):
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
