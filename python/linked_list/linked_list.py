class Node:

    def __init__(self, value, next=None):
        self.value = value
        self.next = None

class LinkedList:
    """
    Create a Node class that has properties for the value stored in the Node, and a pointer to the next Node.
    """

    def __init__(self, head, values=None):
        # initialization here
        self.head = head

    def insert(self, value):
        node = Node(value)

        if self.head is not None:
            node.next = self.head
        self.head = node


