class Node():
    def __init__(self, value, next = None):
        self.value = value
        self.next = next

class InvalidOperationError(BaseException):
    pass

class PsuedoQueue():
    """[implement standard Queue, with enqueue and dequeue]
    """
    def __init__(self):
        self.first_stack = Stack()
        self.second_stack = Stack()

    def enqueue(self, value):
        """[insert value into first_stack First In First Out]

        Args:
            value ([int])
        """
        self.first_stack.push(value)

    def dequeue(self):
        """[return value from first_stack]

        Raises:
            InvalidOperationError: [description]

        Returns:
            [value]:
        """
        while self.first_stack.peek():
            if self.first_stack.top.next == None:
                return self.first_stack.top.value
            else:
                temp = self.first_stack.pop()
                self.second_stack.push(temp)
                continue

    def is_empty(self):
        if self == None:
            return True
        elif self != None:
            return False

class Stack():
    """[instances of stack have only push, pop, peek methods]
    """
    def __init__(self, node = None):
        self.top = node
        self.next = next

    def push(self, value):
        node = Node(value)
        node.next = self.top
        self.top = node

    def pop(self):
        if self.is_empty():
            raise InvalidOperationError("Method not allowed on empty collection")
        temp = self.top
        self.top = self.top.next
        temp.next = None
        return temp.value

    def peek(self):
        if self.is_empty():
            raise InvalidOperationError("Method not allowed on empty collection")
        return self.top.value

    def is_empty(self):
        if self.top == None:
            return True
        else:
            return False

# if __name__ == '__main__':
#     start = PsuedoQueue()

# # example inputs
#     start.first_stack.push(10)
#     start.first_stack.push(15)
#     start.first_stack.push(20)

# # enqueue test
#     start.enqueue(5)
#     print(start.dequeue())