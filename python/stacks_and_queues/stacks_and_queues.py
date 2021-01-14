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
        temp = self.top
        self.top = self.top.next
        temp.next = None
        return temp.value

    def peek(self):
        if self.is_empty():
            raise InvalidOperationError("Method not allowed on empty collection")
        return self.top.value

    def is_empty(self):
        # input -> none
        # output -> boolean
        if self.top == None:
            return True
        else:
            return False

class Queue():

    def __init__(self, node = None):
        self.front = None
        self.rear = None

    def enqueue(self, value):
        node = Node(value)
        if not self.rear:
            self.front = node
            self.rear = node
        else:
            self.rear.next = node
            self.rear  = node
    
    def dequeue(self):
        if self.is_empty():
            raise InvalidOperationError("Method not allowed on empty collection")
        temp = self.front
        self.front = self.front.next
        temp.next = None

        return temp.value

    def peek(self):
        if self.is_empty():
            raise InvalidOperationError("Method not allowed on empty collection")
        return self.front.value

    def is_empty(self):
        if self.front == None:
            return True
        elif self.front != None:
            return False
            