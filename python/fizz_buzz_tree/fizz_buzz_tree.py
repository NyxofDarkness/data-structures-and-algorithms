# Write a function called FizzBuzzTree which takes a k-ary tree as an argument.
# Without utilizing any of the built-in methods available to your language, determine whether or not the value of each node is divisible by 3, 5 or both. Create a new tree with the same structure as the original, but the values modified as follows:
# If the value is divisible by 3, replace the value with “Fizz”
# If the value is divisible by 5, replace the value with “Buzz”
# If the value is divisible by 3 and 5, replace the value with “FizzBuzz”
# If the value is not divisible by 3 or 5, simply turn the number into a String.
# Return a new tree.
from tree.tree import Node, BinaryTree, BinarySearchTree
from stacks_and_queues.stacks_and_queues import Queue

def fizz_buzz_additions(value):
    """[replaces value with Fizzbuzz, Buzz, Fizz, or as a string]

    Args:
        value ([int]): [value]

    Returns:
        [string]: [either words depending on divisibility, or a string of int]
    """
    if value % 15 == 0:
        return "FizzBuzz"
    elif value % 5 == 0:
        return "Buzz"
    elif value % 3 == 0:
        return "Fizz"
    else:
        return str(value)

class Tree:
    def __init__(self):
        self.root = None

class Node_Situation:
    def __init__(self, value):
        self.value = ValueError
        self.child = []

def FizzBuzzTree(tree):
    # traverse nodes, on at a time
    # compare nodes, if divisible by 3 replace node.value with Fizz, 5 replace node.value with Buzz, both can be added
    # else add node to string
    # return new BinaryTree
    return_tree = Tree()
    temp = Queue()
    if tree.root:
        temp.enqueue(tree.root)
        return_tree.root = Node_Situation(fizz_buzz_additions(tree.root.value))
    while not temp.is_empty():
        temp_away = temp.dequeue()
        for child in temp_away.child:
            return_tree.root.child.append(Node_Situation(fizz_buzz_additions(child.value)))
            if child.child:
                temp.enqueue(child)


if __name__ == "__main__":
    tree = Tree()
    tree.root = Node_Situation(1)
    tree.root.child.append(Node_Situation(1))

    # get_tree = BinaryTree()
    # root_string = ""

    # def traverse(root):
    #     if root is None:
    #         return
    #         print(f'root value: {root.value}')
        
    #     for i in root:
    #         if (i % 3 == 0) and (i % 5 == 0):
    #             fizzybuzzingel = Node('FizzBuzz')
    #             fizzybuzzingel.left = root.left
    #             fizzybuzzingel.right = root.right
    #             get_tree.root = fizzybuzzingel
    #         elif root.value % 3 == 0:
    #             buzz = Node('Buzz')
    #             buzz.left = root.left
    #             buzz.right = root.right
    #             get_tree.root = buzz
    #         elif root.value % 5 == 0:
    #             fizz = Node('Fizz')
    #             fizz.left = root.left
    #             fizz.right = root.right
    #             get_tree.root = fizz
    #         else:
    #             get_tree.root = root_string

            
            
