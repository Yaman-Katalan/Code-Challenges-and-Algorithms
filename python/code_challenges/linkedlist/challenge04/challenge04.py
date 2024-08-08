# Write here the code challenge solution
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        
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

    def get_reverse(self):
        """
        This method is used to reverse the LinkedList.
        """
        current = self.head
        values = []
        while current is not None:
            values.append(current.value)
            current = current.next
        values.reverse()
        print(f"Reversed List: {values}")
        return values

    def get_status(self):
        print(f"values: {self.__str__()}")
        print(f"length: {self.__len__()}")

    def __str__(self):
        current = self.head
        values = []
        while current is not None:
            values.append(current.value)
            current = current.next
        return str(values)
    
    def __len__(self):
        current=self.head
        count = 0
        while current is not None:
            count+=1
            current = current.next
        return count
    
    def __getitem__(self, index):
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

linked_list.get_status()
linked_list.get_reverse()