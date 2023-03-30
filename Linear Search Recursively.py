'''Given an array of length N and an integer x, you need to find if x is present in the array or not. Return true or false.
Do this recursively.
Input Format

Line 1 : An Integer N i.e. size of array
Line 2 : N integers which are elements of the array, separated by spaces
Line 3 : Integer x
Constraints

1 <= N <= 10^3

Output Format

true or false

Sample Input 0

3
9 8 10
8
Sample Output 0

true
Sample Input 1

3
9 8 10
2
Sample Output 1

false'''

def search(n, arr, x, index = 0):
    
    if index == n:
        return 
    if arr[index] == x:
        return True
    else:
        return search(n, arr, x, index + 1)

n = int(input())
arr = list(map(int, input().split()))
x = int(input())
check = search(n, arr, x)
if check is True:
    print('true')
else:
    print('false')