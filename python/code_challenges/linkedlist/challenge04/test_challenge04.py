# Write your test here
from challenge04 import LinkedList

def test_get_reverse():
    tested_list = LinkedList()
    tested_list.append(1)
    tested_list.append(3)
    tested_list.append(5)
    tested_list.append(7)
    tested_list.append(9)

    actual = tested_list.get_reverse()
    expected = [9,7,5,3,1]
    assert actual == expected