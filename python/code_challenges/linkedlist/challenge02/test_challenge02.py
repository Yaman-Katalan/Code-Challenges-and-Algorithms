# Write your test here
from challenge02 import LinkedList

def test_get_middle_node1():
    tested_list = LinkedList()
    tested_list.append(1)
    tested_list.append(3)
    tested_list.append(5)
    tested_list.append(7)
    tested_list.append(9)
    actual = tested_list.get_middle_node()
    expected = 5
    assert actual == expected

def test_get_middle_node2():
    tested_list = LinkedList()
    tested_list.append(1)
    tested_list.append(3)
    tested_list.append(5)
    tested_list.append(7)
    tested_list.append(9)
    tested_list.append(11)
    actual = tested_list.get_middle_node()
    expected = (5, 7)
    assert actual == expected

