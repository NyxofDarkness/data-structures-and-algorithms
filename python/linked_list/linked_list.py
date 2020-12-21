class Node:

    def __init__(self, value, next=None):
        self.value = value
        self.next = None

    def __str__(self):
        return f"{self.value}"

class LinkedList:
    """
    Create a Node class that has properties for the value stored in the Node, and a pointer to the next Node.
    """

    def __init__(self, value=None):
        # initialization here
        self.head = None 
        if not value is None:
            node = Node(value)
            self.head = node

    def insert(self, value):
        node = Node(value)

        if self.head is not None:
            node.next = self.head
        self.head = node

    def includes(self, value):
        if self.value is not None:
            return True
        else:
            return False

    def __str__():
        nodes = []
        if self.value is not None:
            nodes.append(self.value)
        else:
            print(nodes)
            