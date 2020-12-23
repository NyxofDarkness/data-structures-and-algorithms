class Node:

    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class LinkedList:
    """
    Create a Node class that has properties for the value stored in the Node, and a pointer to the next Node.
    """

    def __init__(self, head=None):
        self.head = head

    def __str__(self):
        output = ''
        current = self.head

        while current is not None:
            output += f'{{ {current.value} }} -> '
            current = current.next
        return output + 'None'
# check this later... none or null? 
    def insert(self, value):
        node = Node(value)

        if self.head is not None:
            node.next = self.head
        self.head = node

    def includes(self, value):
        current = self.head

        while current is not None:
            if current.value == value:
                return True
            current = current.next

        return False

    def append(self, value):
        """[summary]

        Args:
            value ([type]): [description]

        Returns:
            [type]: [description]
        """
        new_node = Node(value)
        current = self.head
        if current is None:
            current = new_node
            return self.head
        while current.next is not None:
            current = current.next
        
        current.next = new_node

    def insert_before(self, value, new_value):
        new_node = Node(new_value)
        current = self.head
        
        if current is None:
            self.insert(new_node)
            return
        while current.next is not None:
            if current.next.value == value:
                new_node.next = current.next
                current.next = new_node
            current = current.next
            return

    def insert_many(self):
        new_linked = []
        current = self.head
        for value in range(1, 5):
            self.insert(value)
            new_linked.append(current.value)
            current = current.next

        return(new_linked)

if __name__ == "__main__":
    new_node = Node(1)
    new_link = LinkedList()
    print(new_link)

# tests the implementation
    new_link = LinkedList(new_node)
    new_link.insert(2)
    print(new_link.includes(2))
    print(new_link.includes(100))
    print(new_link.append(10))
    print(new_link)
    print(new_node)

