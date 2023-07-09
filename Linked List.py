class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def print_LL(self):
        n = self.head
        if n is None:
            print('Linked List is empty')
        else:
            while n is not None:
                print(n.data)
                n = n.next

    def add_begin(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

ll = LinkedList()
ll.add_begin(10)
ll.add_begin(20)
ll.add_begin(44)
ll.add_begin(50)
ll.print_ll()
