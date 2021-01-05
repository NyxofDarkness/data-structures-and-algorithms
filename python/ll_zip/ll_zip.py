class LinkedList(object):
    def __init__(self):
        self.head = None
    class Node(object):
        def __init__(self, d):
            self.data = d
            self.next = None

    def push(self, new_stuff):
        new_node = self.Node(new_stuff)
        new_node.next = self.head
        self.head = new_node

    def zip_lists(self, list2):
        list1_current = self.head
        list2_current = list2.head

        while list1_current != None and list2_current != None:

            list1_next = list1_current.next
            list2_next = list2_current.next

            list2_current.next = list1_next
            list1_current.next = list2_next

            list1_current = list1_next
            list2_current = list2_next
        list2.head = list2_current

# driver programs
llist1 = LinkedList()
llist2 = LinkedList()
llist1.push(1)
llist1.push(3)
llist1.push(2)
print(llist1)

llist2.push(5)
llist2.push(9)
llist2.push(4)
print(llist2)

print(llist1.zip_lists(llist2))