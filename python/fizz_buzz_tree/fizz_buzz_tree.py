# from stacks_and_queues import Queue


# from stacks_and_queues.stacks_and_queues import Queue
# from stacks_and_queues.stacks_and_queues import Queue, Node
from tree.tree import Node



class Node_Situation:
    def __init__(self, value):
        self.value = value
        self.child = []

class Tree_situation:
    def __init__(self, root=None, value=None):
        self.root = root
        # self.right = None
        # self.left = None
        # self.value = value

    def fizzBuzzTree(self):
        node_values = []

        if self.root:
            fizz_buzz_tree = Tree_situation(Tree_situation.fizz_buzz_additions(self.root))
        else:
            return 'Your tree is empty.'

        def traverse(node):
            node_values.append(node.value)
            child_val = []
            new_node = Node_Situation(node.value)

            for child in node.child:
                child = Tree_situation.fizz_buzz_additions(child)
                child_val.append(child.value)
                traverse(child)

            for i in range(len(child_val)):
                new_node.child.append(Node_Situation(child_val[i]))

        traverse(self.root)
        return fizz_buzz_tree, node_values

    @staticmethod
    def fizz_buzz_additions(f_b):
        """[replaces value with Fizzbuzz, Buzz, Fizz, or as a string]

    Args:
        value ([int]): [value]

    Returns:
        [string]: [either words depending on divisibility, or a string of int]
    """
        if f_b.value % 3 == 0 and f_b.value % 5 == 0:
            f_b.value = "FizzBuzz"
        elif f_b.value % 5 == 0:
            f_b.value = "Buzz"
        elif f_b.value % 3 == 0:
            f_b.value = "Fizz"
        else:
            f_b.value = str(f_b.value)
        return f_b
        




if __name__ == "__main__":
    pass
    # tree = Tree()
    # tree.root = Node(1)
    # tree.root.child.append(Node(1))
    # tree.root.child.append(Node(11))
    # tree.root.child.append(Node(111))

    # fizzBuzzTree(tree)


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

            
            
