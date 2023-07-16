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
            print('Linked List is empty')
        else:
            while ptr is not None:
                print(ptr.data, '-->', end=' ')
                ptr = ptr.next

    def print_ll_reverse(self):
        ptr = self.head
        if ptr is None:
            print('Linked List is empty')
        else:
            while ptr.next is not None:
                ptr = ptr.next
            while ptr is not None:
                print(ptr.data, '-->', end=' ')
                ptr = ptr.prev
