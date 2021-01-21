class Node():
    def __init__(self, value, next = None):
        self.value = value
        self.next = next

class InvalidOperationError(BaseException):
    pass

class AnimalShelter():
    """[holds dogs and cats using FIFO approach]
    """
    def __init__(self):
        self.first = None
        self.last = None

    def enqueue(self, value):
        animal = value.lower()
        node = Node(animal)

        if not self.first:
            self.first = node
            self.last = node
        else:
            self.last.next = node
            self.last = node

    def dequeue(self, choice):
        """[add animal to shelter, either dog or cat]

        Args:
            animal ([type]):
        """

        choice = choice.lower()
       
        if self.is_empty():
            raise InvalidOperationError("Method not allowed on empty collection")
        if choice == "cat" or choice == "dog":
            node = self.first
            self.first = self.first.next
            return node.value
        else:
            return "None"

    def is_empty(self):
        if self.first == None:
            return True
        else:
            return False

