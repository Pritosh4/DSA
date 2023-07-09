class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def print_ll(self):
        ptr = self.head
        if ptr is None:
            print('Linked List is empty')
        else:
            while ptr is not None:
                print(ptr.data, '-->', end=' ')
                ptr = ptr.next

    def add_begin(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def add_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            ptr = self.head
            while ptr.next is not None:
                ptr = ptr.next
            ptr.next = new_node

    def add_after(self, data, x):
        new_node = Node(data)
        ptr = self.head
        while ptr is not None and ptr.data != x:
            ptr = ptr.next

        if ptr is None:
            print('That node does not exist')
        else:
            new_node.next = ptr.next
            ptr.next = new_node

    def add_before(self, data, x):
        new_node = Node(data)
        if self.head is None:
            print('Linked List is empty')
        elif self.head.data == x:
            new_node.next = self.head
            self.head = new_node
        else:
            ptr = self.head
            while ptr.next is not None and ptr.next.data != x:
                ptr = ptr.next

            if ptr.next is None:
                print('That node does not exist')
            else:
                new_node.next = ptr.next
                ptr.next = new_nodeptr
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
            ptr = self.head
            while ptr.next.next is not None:
                ptr = ptr.next
            ptr.next = None

    def delete(self, x):
        if self.head is None:
            print('Linked List is empty')
        elif self.head.data == x:
            self.head = self.head.next
        else:
            ptr = self.head
            while ptr.next is not None and ptr.next.data != x:
                ptr = ptr.next
            if ptr.next is None:
                print('Node does not exist')
            else:
                ptr.next = ptr.next.next





ll = LinkedList()
ll.add_begin(10)
ll.add_begin(20)
ll.add_end(40)
ll.add_end(50)
ll.add_after(45, 20)
ll.add_before(5, 20)
ll.del_begin()
ll.del_end()
ll.delete(10)
ll.print_ll()
