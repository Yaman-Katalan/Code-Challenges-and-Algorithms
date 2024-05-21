# Write your test here
from challenge03 import LinkedList

def test_delete_node_1():
    tested_list = LinkedList()
    tested_list.append(1)
    tested_list.append(3)
    tested_list.append(5)
    tested_list.append(7)
    tested_list.append(9)
    tested_list.delete_node(1)
    actual = tested_list.__str__()
    expected = f"{[1,3,5,7]}"
    assert actual == expected

def test_delete_node_2():
    tested_list = LinkedList()
    tested_list.append(1)
    tested_list.append(3)
    tested_list.append(5)
    tested_list.append(7)
    tested_list.append(9)
    tested_list.delete_node(5)
    actual = tested_list.__str__()
    expected = f"{[3,5,7,9]}"
    assert actual == expected

def test_delete_node_3():
    tested_list = LinkedList()
    tested_list.append(1)
    tested_list.append(3)
    tested_list.append(5)
    tested_list.append(7)
    tested_list.append(9)
    tested_list.delete_node(3)
    actual = tested_list.__str__()
    expected = f"{[1,3,7,9]}"
    assert actual == expected

