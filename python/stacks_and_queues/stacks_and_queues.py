class Node():
    def __init__(self, value, next = None):
        self.value = value
        self.next = next

class InvalidOperationError(BaseException):
    pass

class Stack():
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
        node = self.top
        self.top = self.top.next
        return node.value

    def peek(self):
        if self.is_empty():
            raise InvalidOperationError("Method not allowed on empty collection")
        return self.top.value

    def is_empty(self):
        if self.top == None:
            return True
        elif self.top != None:
            return False

class Queue():

    def __init__(self, node = None):
        self.front = node
        self.rear = None

    def enqueue(self, value):
        node = Node(value)
        node.next = self.front
        self.front  = node
    
    def dequeue(self):
        if self.is_empty():
            raise InvalidOperationError("Method not allowed on empty collection")
        node = self.rear
        # self.rear = self.rear.next
        return node.value

    def peek(self):
        if self.is_empty():
            raise InvalidOperationError("Method not allowed on empty collection")
        return self.front.value

    def is_empty(self):
        if self.front == None:
            return True
        elif self.front != None:
            return False