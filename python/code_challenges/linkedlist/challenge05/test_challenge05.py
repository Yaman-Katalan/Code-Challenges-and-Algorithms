# Write your test here

from challenge05 import LinkedList

def test_insert_after():
    tested_list = LinkedList()
    tested_list.append(1)
    tested_list.append(3)
    tested_list.append(5)
    tested_list.append(7)
    tested_list.append(9)

    actual = tested_list.insert_after(3,4)
    expected = [1,3,4,5,7,9]
    assert actual == expected