class Node:
    def __init__(self, value):
        """
        Initialize a node with the given value.
        
        :param value: The value of the node.
        """
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        """
        Initialize an empty LinkedList.
        """
        self.head = None

    def append(self, value):
        """
        Append a new value to the LinkedList.

        :param value: The value to append to the list.
        :return: True if the value was successfully appended, False otherwise.
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

    def delete_node(self, value):
        """
        Delete the first node with the given value from the LinkedList.
        It is guaranteed that the node to be deleted is not the tail node.
        
        :param value: The value of the node to delete.
        :return: True if the node was successfully deleted, False otherwise.
        """
        if self.head is None:
            print("Error: The list is empty.")
            return False

        current = self.head

        # Handle the special case where the head node needs to be deleted
        if current.value == value:
            if current.next is None:
                print("Error: The node to be deleted is the only node in the list or is a tail node.")
                return False
            self.head = current.next
            return True
        
        # Traverse the list to find the node to delete
        while current.next and current.next.value != value:
            current = current.next
        
        # If the node to delete is found
        if current.next:
            # Check if it is a tail node (which should not be the case as per constraints)
            if current.next.next is None:
                print("Error: The node to be deleted is the tail node.")
                return False
            current.next = current.next.next
            return True
        
        print("Error: Node with the given value not found.")
        return False

    def __str__(self):
        """
        Return a string representation of the LinkedList.
        
        :return: A string representing the LinkedList.
        """
        current = self.head
        values = []
        while current is not None:
            values.append(current.value)
            current = current.next
        return str(values)

# Example Usage
linked_list = LinkedList()
linked_list.append(5)
linked_list.append(10)
linked_list.append(15)

print("Initial list:")
print(linked_list)

# Deleting the node with value 10
if linked_list.delete_node(10):
    print("List after deleting node with value 10:")
    print(linked_list)

# Trying to delete a non-existent node (for demonstration purposes)
if linked_list.delete_node(20):
    print("List after attempting to delete node with value 20:")
    print(linked_list)
