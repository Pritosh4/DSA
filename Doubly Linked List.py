class Node:
    def __init__(self, data):
        self.prev = None
        self.data = data
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def print_ll(self):
        ptr = self.head
        if ptr is None:
            print('Doubly Linked List is empty')
        else:
            while ptr is not None:
                print(ptr.data, '-->', end=' ')
                ptr = ptr.next

    def print_ll_reverse(self):
        ptr = self.head
        if ptr is None:
            print('Doubly Linked List is empty')
        else:
            while ptr.next is not None:
                ptr = ptr.next
            while ptr is not None:
                print(ptr.data, '-->', end=' ')
                ptr = ptr.prev

    def add_begin(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
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
            new_node.prev = ptr

    def add_after(self, data, x):
        new_node = Node(data)
        if self.head is None:
            print('Doubly Linked List is empty')
        else:
            ptr = self.head
            while ptr is not None and ptr.data != x:
                ptr = ptr.next

            if ptr is None:
                print('That node does not exist')
            else:
                new_node.next = ptr.next
                new_node.prev = ptr
                if ptr.next:
                    ptr.next.prev = new_node
                ptr.next = new_node

    def add_before(self, data, x):
        new_node = Node(data)
        if self.head is None:
            print('Doubly Linked List is empty')
        else:
            ptr = self.head
            while ptr is not None and ptr.data != x:
                ptr = ptr.next

            if ptr is None:
                print('That node does not exist')
            else:
                new_node.next = ptr
                new_node.prev = ptr.prev
                if ptr.prev:
                    ptr.prev.next = new_node
                else:
                    self.head = new_node
                ptr.prev = new_node
    def del_begin(self):
        if self.head:
            self.head = self.head.next
            self.head.prev = None
        else:
            print('Doubly Linked List is empty')

    def del_end(self):
        if self.head is None:
            print('Doubly Linked List is empty')
        elif self.head.next is None:
            self.head = None
        else:
            ptr = self.head
            while ptr.next is not None:
                ptr = ptr.next
            ptr.prev.next = None

    def delete(self, x):
        if self.head is None:
            print('Doubly Linked List is empty')

        elif self.head.data == x:
            print('yes 1')
            self.head = self.head.next
            if self.head:
                self.head.prev = None
        else:
            ptr = self.head
            while ptr.next is not None:
                if ptr.data == x:
                    break
                ptr = ptr.next

            if ptr.next is not None:
                ptr.next.prev = ptr.prev
                ptr.prev.next = ptr.next

            else:
                if ptr.data == x:
                    ptr.prev.next = None
                else:
                    print('Node does not exist')


dll = DoublyLinkedList()
dll.add_begin(10)
dll.add_begin(20)
dll.add_end(40)
dll.add_end(50)
dll.add_after(45, 20)
dll.add_before(5, 20)
dll.del_begin()
dll.del_end()
dll.delete(45)
dll.print_ll()
dll.print_ll_reverse()
