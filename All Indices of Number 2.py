'''Given an array of length N and an integer x, you need to find all the indexes where x is present in the input array. Save all the indexes in an array (in increasing order).
Do this recursively. Indexing in the array starts from 0.
Input Format

Line 1 : An Integer N i.e. size of array
Line 2 : N integers which are elements of the array, separated by spaces
Line 3 : Integer x
Constraints

1 <= N <= 10^3
Output Format

indexes where x is present in the array (separated by space)
Sample Input 0

5
9 8 10 8 8
8
Sample Output 0

1 3 4
Sample Input 1

5
9 8 10 8 8
9
Sample Output 1

0'''

def indices(n, arr, x, index = 0):
    if index == n:
        return 0
    elif arr[index] == x:
        print(index, end=' ')
    return indices(n, arr, x, index + 1)
        
    
n = int(input())
arr = list(map(int, input().split()))
x = int(input())
indices(n, arr, x)
