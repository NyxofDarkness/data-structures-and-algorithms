class Node:
    def __init__(self, value = None, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right

class BinaryTree:
    def __init__(self, root = None):
        self.root = root

# Define these method 
    def pre_order(self):
        order = []
        def traverse(root):
            if not root:
                return "Nothing here sadly"
            order.append(root.value)
            traverse(root.left)
            traverse(root.right)
        traverse(self.root)
        return order
        # def traverse(root):
        #     if root.left is not None:
        #         traverse(root.left.value)
        #         print(root.left.value)
        #     if root.right is not None:
        #         traverse(root.right.value)
        #     if not root:
        #         return "Nothing here sadly"
        # #     traverse(root.value)
        # #     traverse(root.right)
        # traverse(self.root)

    def in_order(self):
        in_order = []
        def traverse(root):
            # if not root:
            #     return "Nothing here sadly"
            # in_order.append(root.value)
            # else:
                if root.left:
                    traverse(root.left)
                in_order.append(root.value)
                if root.right:
                    traverse(root.right)
        traverse(self.root)
        return in_order

    def post_order (self):
        post_order = []
        def traverse(root):
            if not root:
                return "Nothing here sadly"
            traverse(root.left)
            traverse(root.right)
            post_order.append(root.value)
        traverse(self.root)
        return post_order

# which returns an array of the values, ordered appropriately.
# Any exceptions or errors that come from your code should be semantic, capturable errors. For example, rather than a default error thrown by your language, your code should raise/throw a custom, semantic error that describes what went wrong in calling the methods you wrote for this lab.

class BinarySearchTree(BinaryTree):
    def contains(self, value):
        def traverse(node):
            
# Define a method named add that accepts a value, and adds a new node with that value in the correct location in the binary search tree.
# Define a method named contains that accepts a value, and returns a boolean indicating whether or not the value is in the tree at least once.
    def contains(self, val):
        if self.root == val:
            return True
        elif self.right == None:
            return False

if __name__ == "__main__":
    pass
