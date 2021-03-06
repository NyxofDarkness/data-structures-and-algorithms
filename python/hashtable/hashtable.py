from linked_list.linked_list import LinkedList

class HashTable:
    """[Used to create and use a hashtable]
    """

    def __init__(self, size=1024):
        """[creates the instance of a hashtable]

        Args:
            size (int, optional): [sets a length of hastable]. Defaults to 1024.
        """
        self.size = size
        self._buckets = self.size * [LinkedList()]

    def _hash(self, key):
        """[takes in an arbitrary key and returns an index in the collection.]

        Args:
            key ([type]): [returns index in collection]
        """
        sum = 0
        for ch in key:
            sum += ord(ch)

        primed = sum * 19

        index = primed % self.size

        return index
    
    def add(self, key, value):
        """[takes in both the key and value. This method should hash the key, and add the key and value pair to the table, handling collisions as needed.]
        """
        hashed_index = self._hash(key)

        if self.contains(key):
            raise KeyError(f'hashtable contain key: {key} ')
        else:
        #     self._buckets[hashed_index] = LinkedList()

        # self._buckets[hashed_index].add((key, value))
            self._buckets[hashed_index].insert((key, value))

    def get(self, key):
        """[ takes in the key and returns the value from the table.]
        """
        bucket = self._buckets[self._hash(key)]
        
        if not self.contains(key):
            raise ValueError(f'hashtable does not contain {key} ')

        current = bucket.head
        while current:
            if current.value[0] == key:
                return current.value[1]
            else:
                current = current.next

    def contains(self, key):
        """[takes in the key and returns a boolean, indicating if the key exists in the table already.]
        """
        bucket = self._buckets[self._hash(key)]
        current = bucket.head
        if current == None:
            return False

        while current:
            if current.value[0] == key:
                return True
            else:
                current = current.next

        return False
