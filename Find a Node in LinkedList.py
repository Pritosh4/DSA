'''Given a singly linked list of integers and an integer n, find and return the index for the first occurrence of 'n' in the linked list. -1 otherwise.
Note : Assume that the Indexing for the linked list always starts from 0.
Input Format

The first line of each test case or query contains the elements of the singly linked list separated by a single space.
The second line of input contains a single integer depicting the value of 'n'.
Remember/Consider :
While specifying the list elements for input, -1 indicates the end of the singly linked list and hence, would never be a list element
Constraints

0 <= M <= 10^5
Where M is the size of the singly linked list.
Time Limit: 1sec
Output Format

Output for every test case will be printed in a seperate line.
Sample Input 0

3 4 5 2 6 1 9 -1
100
Sample Output 0

-1
Sample Input 1

10 20010 30 400 600 -1
20010
Sample Output 1

1
'''






class Node:
    def __init__(self, val = 0):
        self.val = val
        self.next = None 
        
def insert(head, item):
    temp = Node(item)
    if head is None:
        head = temp
    else:
        ptr = head
        while ptr.next:
            ptr = ptr.next
        ptr.next = temp    
    return head
        
def array_to_ll(arr):
    head = None
    for i in range(len(arr)):
        head = insert(head, arr[i])
    return head

def find(ptr, num):
    count = 0
    while ptr.next:
        if ptr.val == num:
            return count
        count += 1
        ptr = ptr.next
    return -1

arr = list(map(int, input().split()))
num = int(input())
head = array_to_ll(arr)
print(find(head, num))


