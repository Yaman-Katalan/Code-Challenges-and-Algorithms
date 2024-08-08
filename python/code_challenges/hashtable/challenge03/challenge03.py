class Node:
    def __init__(self, key, value):
        """
        Initializes a Node with the given key and value, and sets the next node to None.
        """
        self.key = key
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        """
        Initializes an empty LinkedList.
        """
        self.head = None

    def insert(self, key, value):
        """
        Inserts a node with the given key and value into the LinkedList.
        """
        new_node = Node(key, value)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def find(self, key):
        """
        Finds and returns the node with the given key in the LinkedList.
        """
        current = self.head
        while current:
            if current.key == key:
                return current
            current = current.next
        return None

    def __iter__(self):
        """
        Allows iteration over the LinkedList.
        """
        current = self.head
        while current:
            yield current
            current = current.next

class HashTable:
    def __init__(self, size=10):
        """
        Initializes a HashTable with the specified size.
        """
        self.size = size
        self.table = [None] * size

    def _hash(self, key):
        """
        Generates a hash for the given key.
        """
        return hash(key) % self.size

    def set(self, key, value):
        """
        Sets the key-value pair in the HashTable.
        """
        index = self._hash(key)
        if self.table[index] is None:
            self.table[index] = LinkedList()
            self.table[index].insert(key, value)
        else:
            existing_node = self.table[index].find(key)
            if existing_node:
                existing_node.value = value
            else:
                self.table[index].insert(key, value)

    def get(self, key):
        """
        Retrieves the value associated with the given key in the HashTable.
        """
        index = self._hash(key)
        if self.table[index] is None:
            return None
        else:
            node = self.table[index].find(key)
            if node:
                return node.value
            return None

def sum_of_unique_elements(nums):
    """
    Finds the summation of unique elements in the array using a HashTable.
    """
    hash_table = HashTable()

    # Populate the hash table with the frequency of each element
    for num in nums:
        current_count = hash_table.get(num)
        if current_count is None:
            hash_table.set(num, 1)
        else:
            hash_table.set(num, current_count + 1)

    # Sum the elements that appear exactly once
    unique_sum = 0
    for num in nums:
        if hash_table.get(num) == 1:
            unique_sum += num

    return unique_sum

# Test cases
if __name__ == "__main__":
    nums_1 = [1, 2, 3, 2]  # Output: 4
    nums_2 = [1, 2, 3, 4, 5]  # Output: 15
    nums_3 = [1, 1, 2, 2, 3, 3]  # Output: 0
    nums_4 = [1, 2, 2, 3, 4, 4, 5]  # Output: 9
    nums_5 = [42]  # Output: 42

    print(sum_of_unique_elements(nums_1))
    print(sum_of_unique_elements(nums_2))
    print(sum_of_unique_elements(nums_3))
    print(sum_of_unique_elements(nums_4))
    print(sum_of_unique_elements(nums_5))
