class Node:
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class BinaryTree:
    def __init__(self, root=None):
        self.root = root
# Define these method 
    def pre_order(self):
        pass

    def in_order(self):
        pass

    def post_order (self):
        pass

# which returns an array of the values, ordered appropriately.
# Any exceptions or errors that come from your code should be semantic, capturable errors. For example, rather than a default error thrown by your language, your code should raise/throw a custom, semantic error that describes what went wrong in calling the methods you wrote for this lab.

class BinarySearchTree(BinaryTree):
    pass

    def add(self, value):
        pass
# Define a method named add that accepts a value, and adds a new node with that value in the correct location in the binary search tree.
# Define a method named contains that accepts a value, and returns a boolean indicating whether or not the value is in the tree at least once.
if __name__ == "__main__":
    pass
