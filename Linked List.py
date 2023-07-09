class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def print_ll(self):
        n = self.head
        if n is None:
            print('Linked List is empty')
        else:
            while n is not None:
                print(n.data, '-->', end=' ')
                n = n.next

    def add_begin(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def add_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.next is not None:
                n = n.next
            n.next = new_node

ll = LinkedList()
ll.add_begin(10)
ll.add_begin(20)
ll.add_end(40)
ll.add_end(50)
ll.print_ll()
