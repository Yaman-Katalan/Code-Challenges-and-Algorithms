import pytest
from challenge01 import LinkedList, Node  # Replace 'your_module' with the actual name of your module

def test_append():
    """Test appending values to the LinkedList."""
    linked_list = LinkedList()
    assert linked_list.append(5) is True
    assert linked_list.append(10) is True
    assert linked_list.append(15) is True
    assert linked_list.append(5) is False  # Duplicate value
    assert linked_list.append(-10000) is False  # Out of range

    assert str(linked_list) == "[5, 10, 15]"

def test_delete_node():
    """Test deleting nodes from the LinkedList."""
    linked_list = LinkedList()
    linked_list.append(5)
    linked_list.append(10)
    linked_list.append(15)
    
    # Delete node with value 10
    assert linked_list.delete_node(10) is True
    assert str(linked_list) == "[5, 15]"

    # Try deleting a node that does not exist
    assert linked_list.delete_node(20) is False
    assert str(linked_list) == "[5, 15]"

    # Try deleting the head node (value 5)
    assert linked_list.delete_node(5) is True
    assert str(linked_list) == "[15]"

    # Try deleting the only remaining node (value 15)
    # This should not be allowed as per the constraints, and thus should return False
    assert linked_list.delete_node(15) is False
    assert str(linked_list) == "[15]"

def test_delete_tail_node():
    """Test that deletion of a tail node is not allowed."""
    linked_list = LinkedList()
    linked_list.append(5)
    linked_list.append(10)
    
    # Try deleting the tail node (value 10)
    assert linked_list.delete_node(10) is False
    assert str(linked_list) == "[5, 10]"

if __name__ == "__main__":
    pytest.main()
