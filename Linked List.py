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

    def add_after(self, data, x):
        new_node = Node(data)
        n = self.head
        while n is not None and n.data != x:
            n = n.next

        if n is None:
            print('That node does not exist')
        else:
            new_node.next = n.next
            n.next = new_node

    def add_before(self, data, x):
        new_node = Node(data)
        if self.head is None:
            print('Linked List is empty')
        elif self.head.data == x:
            new_node.next = self.head
            self.head = new_node
        else:
            n = self.head
            while n.next is not None and n.next.data != x:
                n = n.next

            if n.next is None:
                print('That node does not exist')
            else:
                new_node.next = n.next
                n.next = new_node

    def del_begin(self):
        if self.head:
            self.head = self.head.next
        else:
            print('Linked List is empty')

    def del_end(self):
        if self.head is None:
            print('Linked List is empty')
        elif self.head.next is None:
            self.head = None
        else:
            n = self.head
            while n.next.next is not None:
                n = n.next
            n.next = None




ll = LinkedList()
ll.add_begin(10)
ll.add_begin(20)
ll.add_end(40)
ll.add_end(50)
ll.add_after(45, 20)
ll.add_before(5, 20)
ll.del_begin()
ll.del_end()
ll.print_ll()
