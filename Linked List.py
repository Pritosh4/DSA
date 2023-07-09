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

LL = LinkedList()
LL.print_LL()
