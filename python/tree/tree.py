class Node:
    """[node with two pointers for a binary tree, inserts Node approprietly]
    """
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    """[Creates empty binary tree, and holds methods for moving around that tree]
    """
    def __init__(self):
        self.root = None

# Define these method 
    def pre_order(self):
        def traverse(root, order=[]):
            if not root:
                return
            order.append(root.value)
            if root.left:
                traverse(root.left, order)
            if root.right:
                traverse(root.right, order)
            return order
        return traverse(self.root)

    def in_order(self):
        def traverse(root, order=[]):
            if not root:
                return
            if root.left:
                traverse(root.left, order)
            order.append(root.value)
            if root.right:
                traverse(root.right, order)
            return order
        return traverse(self.root)

    def post_order (self):
        def traverse(root, order=[]):
            if not root:
                return
            if root.left:
                traverse(root.left, order)
            if root.right:
                traverse(root.right, order)
            order.append(root.value)
            return order
        return traverse(self.root)
    
# which returns an array of the values, ordered appropriately.
# Any exceptions or errors that come from your code should be semantic, capturable errors. For example, rather than a default error thrown by your language, your code should raise/throw a custom, semantic error that describes what went wrong in calling the methods you wrote for this lab.

class BinarySearchTree(BinaryTree):
    """[methods for binary search acxross tree nodes]

    Args:
        BinaryTree ([inherit]): [methods for moving around nodes inherited from here]
    """
    def __init__(self):
        self.root = None
    
    def add(self, val):
        if not self.root:
            self.root = Node(val)
            return

        def traverse(root, val):
            if not root:
                return
            if root.value == val:
                raise ValueError(f'{val} is already here it seems...')

            if val < root.value:
                if root.left == None:
                    root.left = Node(val)
                    return
                else:
                    traverse(root.left, val)
                if val > root.value:
                    if root.right == None:
                        root.right = Node(val)
                        return
                    else:
                        traverse(self.root, val)

        traverse(self.root, val)
        return
                
            
# Define a method named add that accepts a value, and adds a new node with that value in the correct location in the binary search tree.
# Define a method named contains that accepts a value, and returns a boolean indicating whether or not the value is in the tree at least once.
    def contains(self, val):

        val = [val]
        def traverse(root, val):
            
            if not root:
                return
            if root.value == val[0]:
                val.append(True)
                return val
            if val[0] < root.value and root.left:
                traverse(root.left, val)
            if val[0] > root.value and root.right:
                traverse(root.right, val)
            val.append(False)

            return val
        return traverse(self.root, val)[1]

# if __name__ == "__main__":
#     pass

# root = Node(27)
# root.insert(14)
# root.insert(35)
# root.insert(10)