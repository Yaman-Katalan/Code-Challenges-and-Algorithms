# Write here the code challenge solution
class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None

    def size(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)

def delete_middle(stack):
    if stack.is_empty():
        return stack

    middle_index = stack.size() // 2  # Find the middle index
    temp_stack = Stack()
    
    # Pop the elements until the middle one is reached
    for _ in range(middle_index):
        temp_stack.push(stack.pop())

    # Pop the middle element (do not push it to temp_stack)
    stack.pop()

    # Push the elements back from temp_stack to the original stack
    while not temp_stack.is_empty():
        stack.push(temp_stack.pop())

    return stack

# Testing the function with examples
stack1 = Stack()
for i in [1, 2, 3, 4, 5]:
    stack1.push(i)
print("Original Stack 1:", stack1)
stack1 = delete_middle(stack1)
print("Stack 1 after deleting middle element:", stack1)

stack2 = Stack()
for i in [1, 2, 3, 4]:
    stack2.push(i)
print("Original Stack 2:", stack2)
stack2 = delete_middle(stack2)
print("Stack 2 after deleting middle element:", stack2)
