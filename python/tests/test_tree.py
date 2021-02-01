import pytest
from tree.tree import Node, BinaryTree, BinarySearchTree

# Can successfully instantiate an empty tree
def test_tree():
    tree = BinaryTree()
    actual = tree.root
    expected = None
    assert actual == expected

# Can successfully instantiate a tree with a single root node
def test_single_root_tree():
    tree = BinaryTree()
    tree.root = Node(11)
    actual = tree.root.value
    expected = 11
    assert actual == expected

#  Can successfully add a left child and right child to a single root node
def test_add_left_and_right():
    tree = BinaryTree()
    tree.root = Node(111)
    tree.root.left = Node(11)
    tree.root.right = Node(1)
    actual = f"{tree.root.value}, {tree.left.value}, {tree.right.value}"
    expected = "111, 11, 1"
    assert actual == expected

# Can successfully return a collection from a preorder traversal
def test_tree_preorder():
    tree = BinaryTree()
    tree.root = Node(1)
    tree.root.left = Node(11)
    tree.root.right = Node(111)
    tree.root.left.left = Node (1111)
    tree.root.left.right = Node(11111)
    actual = tree.pre_order()
    expected = [1, 11, 1111, 11111, 111]
    assert actual == expected

# Can successfully return a collection from an inorder traversal
def test_tree_inorder():
    tree = BinaryTree()
    tree.root = Node(1)
    tree.root.left = Node(11)
    tree.root.right = Node(2)
    tree.root.left.left = Node(111)
    tree.root.right.right = Node(22)
    actual = tree.in_order()
    assert actual == expected

# Can successfully return a collection from a postorder traversal
def test_tree_postorder():
    tree = BinaryTree()
    tree.root = Node(1)
    tree.root.left = Node(11)
    tree.root.right = Node(2)
    tree.root.left.left = Node(111)
    tree.root.left.right = Node(112)
    actual = tree.post_order()
    assert actual == expected