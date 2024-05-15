# Write your test here

from challenge01 import LinkedList

def test_append():
    tested_list = LinkedList()
    actual = tested_list.append(2)
    expected = True
    assert actual == expected


def test_delete():
    tested_list = LinkedList()
    tested_list.append(7)
    tested_list.append(8)
    tested_list.append(9)
    actual = tested_list.delete_node(tested_list.head.next)
    expected = True
    assert actual == expected