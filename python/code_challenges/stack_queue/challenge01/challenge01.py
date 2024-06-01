# Write here the code challenge solution
class MyQueue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int) -> None:
        """
        This method is used to add new value to the queue.
        """
        self.stack1.append(x)

    def pop(self) -> int:
        """
        This method is used to remove a value from the queue from bottom.
        """
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()

    def peek(self) -> int:
        """
        This method is used to return the first value added.
        """
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2[-1]

    def empty(self) -> bool:
        """
        This method is used to check whther the queue is empty or not.
        """
        return not self.stack1 and not self.stack2

    def __str__(self):
        return f"MyQueue: {self.stack2[::-1] + self.stack1}"

# Example usage:
myQueue = MyQueue()
print(myQueue.push(1))

myQueue.push(2)
myQueue.push(3)
myQueue.push(4)
myQueue.push(5)
print(myQueue)  # Output: MyQueue: [1, 2]
print(myQueue.pop())
print(myQueue.pop())
print(myQueue.pop())
print(myQueue.pop())
