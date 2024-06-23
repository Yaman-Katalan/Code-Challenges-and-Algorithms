# Write here the code challenge solution
class Node:
    def __init__(self, value):
        """
        Initialize a new node with a given value.
        
        :param value: The value to be stored in the node.
        """
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        """
        Initialize an empty linked list.
        """
        self.head = None

    def append(self, value):
        """
        Append a new node with the given value to the end of the linked list.
        
        :param value: The value to be added to the linked list.
        :return: True if the value was successfully added, False otherwise.
        """
        # Check length of LinkedList
        if len(self) >= 100:
            print("Error: list length must be in the range [1, 100].")
            return False

        # Check if value is within range [1, 100]
        if not (1 <= value <= 100):
            print("Error: Value must be within the range [1, 100].")
            return False
        
        # Check if value is unique in the list
        current = self.head
        while current:
            if current.value == value:
                print("Error: Value must be unique in the list.")
                return False
            current = current.next

        node = Node(value) # Create new node.
        
        # If the LinkedList is empty:
        if self.head is None:
            self.head = node
            return True
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = node
            return True
    # Time complexity = O(n)
    # Space complexity = O(1)

    def get_middle_node(self):
        """
        Get the middle value(s) of the linked list.
        
        :return: The middle value if the linked list has an odd length,
                 or a tuple of the two middle values if it has an even length.
        """
        if len(self) % 2 != 0:
            return self[(len(self)-1)//2]
        else:
            return self[(len(self)//2)-1], self[len(self)//2]

    def __str__(self):
        """
        Get a string representation of the linked list.
        
        :return: A string representing the values in the linked list.
        """
        current = self.head
        values = []
        while current is not None:
            values.append(current.value)
            current = current.next
        return str(values)
    
    def __len__(self):
        """
        Get the length of the linked list.
        
        :return: The number of nodes in the linked list.
        """
        current = self.head
        count = 0
        while current is not None:
            count += 1
            current = current.next
        return count
    
    def __getitem__(self, index):
        """
        Get the value at the specified index.
        
        :param index: The index of the value to retrieve.
        :return: The value at the specified index.
        :raises IndexError: If the index is out of range.
        """
        if index < 0:
            raise IndexError("Index out of range")
        current = self.head
        count = 0
        while current is not None:
            if count == index:
                return current.value
            count += 1
            current = current.next
        raise IndexError("Index out of range")
    

linked_list = LinkedList()
linked_list.append(3)
linked_list.append(5)
linked_list.append(7)
linked_list.append(9)
linked_list.append(11)
linked_list.append(13)
# linked_list.append(15)

print(linked_list)
print(len(linked_list))
print(linked_list.get_middle_node())

