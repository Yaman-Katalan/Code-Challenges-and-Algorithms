# Write here the code challenge solution


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        """
        This function is used to append a new value to the LinkedList.
        """
        # Check if value is within range [-1000, 1000]
        if not (-1000 <= value <= 1000):
            print("Error: Value must be within the range [-1000, 1000].")
            return False
        
        # Check if value is unique in the list
        current = self.head
        while current:
            if current.value == value:
                print("Error: Value must be unique in the list.")
                return False
            current = current.next
        
        node = Node(value)  # Create new node.
        
        # If the LinkedList is empty:
        if self.head is None:
            self.head = node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = node
        return True

    def delete_node(self, node):
        """
        This method deletes a node.
        """
        if node.next == None:
            print("Error: Tail Node can't be deleted!")
            return False
        node.value = node.next.value
        node.next = node.next.next
        return True

    def __str__(self):
        """
        This method returns the values of the linked_list.
        """
        current = self.head
        values = []
        while current is not None:
            values.append(current.value)
            current = current.next
        return str(values)


list = LinkedList()
list.append(5)
list.append(5)          # Error: Duplicate
list.append(-10000)     # Error: Out of the range
list.append(10)
list.append(15)
# list.append(20)
# list.append(25)
# list.append(30)

print(list)

list.delete_node(list.head.next.next)
print(list)

# list.delete_node(list.head.next)
# print(list)

# list.delete_node(list.head.next)
# print(list)
