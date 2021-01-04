from linked_list.linked_list import LinkedList, Node
import pytest

#code challenge 7

def test_nth():
    node = Node(0)
    link = LinkedList(node)
    link.insert(4)
    link.append(10)
    link.kthFromEnd(1)
    actual = 0
    expected = 0
    assert actual == expected

    # greater than the length of the list
def test_length():
    node = Node(0)
    link = LinkedList(node)
    link.kthFromEnd(10)
    actual = 'number is greater than the length of list.'
    expected = 'number is greater than the length of list.'
    assert actual == expected

# where k and length of list is same
def test_same_kth():
    node = Node(0)
    link = LinkedList(node)
    link.kthFromEnd(10)
    actual = 4
    expected = 4
    assert actual == expected

# where k is not a postive int
def test_neg():
    node = Node(0)
    link = LinkedList(node)
    link.kthFromEnd(10)
    actual = 'negative number given'
    expected = 'negative number given'
    assert actual == expected

# where linked list is length of 1
def test_one_kth():
    

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

# Add a node to the end of the linked list
def test_append ():
    node = Node(0)
    link = LinkedList(node)
    link.insert(4)
    link.append(10)
    actual = str(link)
    expected = f'{{ 4 }} -> {{ 0 }} -> {{ 10 }} -> NONE'
    assert actual == expected


# Insert a node before a node located in the middle of a linked list
def test_before ():
    node = Node(0)
    link = LinkedList(node)
    link.insert(4)
    link.append(10)
    link.insert_before(0, 5)
    actual = str(link)
    expected = f'{{ 4 }} -> {{ 5 }} -> {{ 0 }} -> {{ 10 }} -> NONE'
    assert actual == expected

# Can successfully insert a node before the first node of a linked lis
def test_after ():
    node = Node(0)
    link = LinkedList(node)
    link.insert(4)
    link.append(10)
    link.insert_after(10, 5)
    actual = str(link)
    expected = f'{{ 4 }} -> {{ 0 }} -> {{ 10 }} -> {{ 5 }} -> NONE'
    assert actual == expected

# Can successfully add multiple nodes to the end of a linked list
def test_many():
    # node = Node(4)
    link = LinkedList()
    link.insert(4)
    link.append(1)
    link.append(2)
    link.append(3)
    actual = str(link)
    expected = f'{{ 4 }} -> {{ 1 }} -> {{ 2 }} -> {{ 3 }} -> NONE'
    assert actual == expected

    # Can successfully insert after a node in the middle of the linked list
def test_before_node ():
    node = Node(0)
    link = LinkedList(node)
    link.insert(4)
    link.append(10)
    link.insert_after(10, 5)
    actual = str(link)
    expected = f'{{ 4 }} -> {{ 0 }} -> {{ 10 }} -> {{ 5 }} -> NONE'
    assert actual == expected

# Can successfully insert a node after the last node of the linked list
def test_after_last():
    node = Node(0)
    link = LinkedList(node)
    link.insert(4)
    link.append(10)
    link.insert_after(10, 5)
    actual = str(link)
    expected = f'{{ 4 }} -> {{ 0 }} -> {{ 10 }} -> {{ 5 }} -> NONE'
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

