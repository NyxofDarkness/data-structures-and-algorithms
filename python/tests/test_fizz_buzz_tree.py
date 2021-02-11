from fizz_buzz_tree.fizz_buzz_tree import Node_Situation, Tree_situation
# from fizz_buzz_tree.fizz_buzz_tree import Tree_situation, Node_Situation

import pytest

@pytest.fixture()
def test_tree():
    """[tree setup for testing]

    Returns:
        [obj]: [object tree for testing]
    """
    node1 = Node_Situation(9) #fizz
    node2 = Node_Situation(4) #fizz
    node3 = Node_Situation(10) #buzz
    node4 = Node_Situation(15) #fizzbuzz

    node1.child.append(node2)
    node1.child.append(node3)
    node1.child.append(node4)

    temp = Tree_situation(node1, node2)

    return temp



def test_whole_tree(test_tree):
    tree = test_tree.fizzBuzzTree()
    actual = tree[1]
    expected = ['Fizz', '4', 'Buzz', 'FizzBuzz']
    assert actual == expected

def test_fizz(test_tree):
    tree, node = test_tree.fizzBuzzTree()
    actual = tree.root.value
    expected = 'Fizz'
    assert actual == expected

def test_buzz(test_tree):
    tree, node = test_tree.fizzBuzzTree()
    actual = tree.root.child[1].value
    expected = 'Buzz'
    assert actual == expected

def test_fizzbuzz(test_tree):
    tree, node = test_tree.fizzBuzzTree()
    actual = tree.root.child[2].value
    expected = 'FizzBuzz'
    assert actual == expected

def test_string(test_tree):
    tree, node = test_tree.fizzBuzzTree()
    actual = tree.root.child[0].value
    expected = '4'
    assert actual == expected

def test_Node_Situation(test_tree):
    assert Node_Situation

def test_Tree_Situation(test_tree):
    assert Tree_situation



# If the value is divisible by 3, replace the value with “Fizz”
# If the value is divisible by 5, replace the value with “Buzz”
# If the value is divisible by 3 and 5, replace the value with “FizzBuzz”
# If the value is not divisible by 3 or 5, simply turn the number into a String.