class Node():
    def __init__(self, cat, dog, next = None):
        self.cat = cat
        self.dog = dog
        self.next = next

class InvalidOperationError(BaseException):
    pass

class AnimalShelter():
    """[holds dogs and cats using FIFO approach]
    """
    def __init__(self):
        self.cat = Stack()
        self.dog = Stack()

    def enqueue(self, cat, dog):
        """[add animal to shelter, either dog or cat]

        Args:
            dog ([type]):
            cat ([type]): 
        """
        if self.cat.top.next == None:
            return self.cat.top.value
        else:
            self.dog.top.next == None
            return self.dog.top.value
