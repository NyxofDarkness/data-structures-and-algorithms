from linked_list.linked_list import LinkedList, Node
import pytest

def test_import():
    assert LinkedList
    assert Node

def test_empty():
    empty_list = LinkedList()
    actual = empty_list.head
    expected = None
    assert actual == expected

def test_insert(generate_new_list):
    generate_new_list.insert(20)
    actual = generate_new_list.head.value
    expected = 20
    assert actual == expected

## need to write returns true, returns false
## returns all values in list

def test_append ():
    node = Node(0)
    link = LinkedList(node)
    link.insert(4)
    link.append(10)
    actual = str(link)
    expected = f'{{ 4 }} -> {{ 0 }} -> {{ 10 }} -> NONE'
    assert actual == expected

def test_before ():
    node = Node(0)
    link = LinkedList(node)
    link.insert(4)
    link.append(10)
    link.insert_before(0, 5)
    actual = str(link)
    expected = f'{{ 4 }} -> {{ 5 }} -> {{ 0 }} -> {{ 10 }} -> NONE'
    assert actual == expected

## fixture for code challenges 5, 6
@pytest.fixture
def generate_new_list():
    node = Node(0)
    new_list = LinkedList(node)
    list_length = 0

    for value in range(1, 5):
        new_list.insert(value)
        list_length += 1

    return new_list

## for code challenge 4

a = Node(4)
b = LinkedList()
c = LinkedList()

def test_one():
    assert (a.value == 4 and a.next is None)

def test_two():
    b.insert(8)
    assert b.head.value == 8

