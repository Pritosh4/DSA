'''You are given an m x n integer matrix matrix with the following two properties:
Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.
You must write a solution in O(log(m * n)) time complexity.
Input Format

First line of each test case or query contains two integer values, 'N' and 'M', separated by a single space. They represent the 'rows' and 'columns' respectively, for the two-dimensional array/list.
Second line onwards, the next 'N' lines or rows represent the ith row values.
Each of the ith row constitutes 'M' column values separated by a single space.
Target Value
Constraints

1 <= t <= 10^2
0 <= N <= 10^3
0 <= M <= 10^3
Time Limit: 1sec
Output Format

Print the elements of the two-dimensional array/list in the spiral form in a single line, separated by a single space.
Sample Input 0

3 
3
1 2 3
4 5 6
7 8 9
3
Sample Output 0

true
Sample Input 1

3
3
1 2 3
4 5 6
7 8 9
10
Sample Output 1

false'''

def search(arr, R, C, target):
    low = 0
    high = R * C - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid // C][mid % C] == target:
            return True
        elif arr[mid // C][mid % C] > target:
            high = mid - 1
        else:
            low = mid + 1
    return False


R = int(input())
C = int(input())
arr = []
for i in range(R):
    arr.append(list(map(int, input().split())))
target = int(input())
    
if search(arr, R, C, target):
    print('true')
else:
    print('false')
    

    
