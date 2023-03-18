'''You have been given a integer array/list(ARR) of size N. In the array you are only having 0, 1 and 2 elements. Write a function to sort the array using this algorithm.

Input Format

First line of each test case or query contains an integer 'N' representing the size of the first array/list.
Second line contains 'N' single space separated integers representing the elements in the array/list.
Constraints

No

Output Format

Return Sorted Array

Sample Input 0

3
0 1 0
Sample Output 0

0 0 1
Sample Input 1

9
0 0 1 1 2 2 2 0 1
Sample Output 1

0 0 0 1 1 1 2 2 2'''

def dutch(arr, n):
    p0 = 0
    p2 = n - 1
    i = 0
    count = 0
    while count < n:
        if arr[i] == 0:
            arr[i], arr[p0] = arr[p0], arr[i]
            i += 1
            p0 += 1
        elif arr[i] == 1:
            i += 1
        else:
            arr[i], arr[p2] = arr[p2], arr[i]
            p2 -= 1
        count += 1
    return arr


n = int(input())
arr = list(map(int, input().split()))
for i in dutch(arr, n):
    print(i, end=' ')
