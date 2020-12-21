from linked_list.linked_list import LinkedList, Node


def test_import():
    assert LinkedList

a = Node(4)
b = LinkedList()

def test_one():
    assert (a.value == 4 and a.next is None)

def test_two():
    b.insert(8)
    assert b.head.value == 8

def test_three():
    