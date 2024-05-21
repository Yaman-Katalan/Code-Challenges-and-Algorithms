# Write here the code challenge solution
# Write here the code challenge solution
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):

        # Check length of LinkedList
        if len(self)>= 30:
            print("Error: list length must be in the range [1, 30].")
            return False

        # Check if value is within range [1, 100]
        if not (0 <= value <= 100):
            print("Error: Value must be within the range [0, 100].")
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

    def get_status(self):
        print(f"values: {self.__str__()}")
        print(f"length: {self.__len__()}")

    def delete_node(self, index):
        if not 1 <= index <=self.__len__():
            print("index out of range!")
            return "There's no such index."
        i = self.__len__() - index
        print(f"i is: {i}")
        print(f"value to be deleted: {self[i]}")
        prev = self.head
        current = self.head.next
        start = self.head

        if i is 0:
            start.value = start.next.value
            start.next = start.next.next
            self.get_status()
            return "First Node Deleted!"

        if i is self.__len__() - 1:
            while start.next.value is not self[i]:
                start = start.next
            start.next = None
            self.get_status()
            return "Tail Deleted!"

        while current.next is not None:
            if current.value is self[i]:
                prev.next = current.next
                current = None
                break

            current = current.next
            prev = prev.next
        self.get_status()


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


linked_list.delete_node(6)
# linked_list.delete_node(2)
# linked_list.delete_node(3)
# linked_list.delete_node(4)