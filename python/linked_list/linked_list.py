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
        return output + 'NONE'

    def insert(self, value):
        node = Node(value)

        if self.head is not None:
            node.next = self.head
        self.head = node

    def includes(self, value):
        """search the linked list with the int given

        Args:
            value ([int]): [given this int if the current's value is equal to it then return True]

        Returns:
            [true/false]: [if given int is in list, return true, else return false]
        """
        current = self.head

        while current is not None:
            if current.value == value:
                return True
            current = current.next

        return False

    def append(self, value):
        """[append a new node]

        Args:
            value ([int]): [number value of node]

        Returns:
            [node]: [new node]
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
        """[Given a value and a new_value, the value should be where we want to insert our new_value as a node before]

        Args:
            value ([int]): [the current.value equals this]
            new_value ([int]): [new node to be inserted]
        """
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

    def insert_after(self, value, new_value):
        """[insert node after]

        Args:
            value ([int]): [value from the linked list]
            new_value ([node]): [mew node created and inserted]

        Return: 
        """
        new_node = Node(new_value)
        current = self.head
        
        if current is None:
            self.insert(new_node)
            return

        while current is not None:
            if current.value == value:
                new_node.next = current.next
                current.next = new_node
                
            current = current.next

       # code challenge 7     
    def kthFromEnd(self, k):
        """[Find the number given from the last of the linked list]

        Args:
            k ([int]): [the nth number from the last of the linked list]

        Returns:
            [int]: [where our new k variable is]
        """
        current = self.head
        length = 0

        if k < 0:
            return 'negative number given'

        while current is not None:
            current = current.next
            length += 1

        if k > length:
            return 'number is greater than the length of list.'
        
        current = self.head
        for num in range(0, length - k):
            current = current.next
        return current.value


if __name__ == "__main__":
    new_node = Node(1)
    new_link = LinkedList()

    print(new_link)

# driver code
    new_link = LinkedList(new_node)
    new_link.insert(2)
    print(new_link.includes(2))
    print(new_link.includes(100))
    print(new_link.append(10))
    print(new_link)
    print(new_node)
    print()

