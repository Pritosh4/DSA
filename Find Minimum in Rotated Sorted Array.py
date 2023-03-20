'''Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

[4,5,6,7,0,1,2] if it was rotated 4 times. [0,1,2,4,5,6,7] if it was rotated 7 times. Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums of unique elements, return the minimum element of this array.

You must write an algorithm that runs in O(log n) time.

Input Format

First line of each test case or query contains an integer 'N' representing the size of the first array/list.
Second line contains 'N' single space separated integers representing the elements in the array/list.
Constraints

n == nums.length
1 <= n <= 5000
Output Format

Minimum element from roatated sorted array
Sample Input 0

5
3 4 5 1 2
Sample Output 0

1
Explanation 0

The original array was [1,2,3,4,5] rotated 3 times.

Sample Input 1

7
4 5 6 7 0 1 2
Sample Output 1

0
Explanation 1

The original array was [0,1,2,4,5,6,7] and it was rotated 4 times'''

def arr_min(arr):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[low] <= arr[high]:
            return arr[low]
        elif mid > 0 and arr[mid] < arr[mid - 1]:
            return arr[mid]
        elif arr[mid] >= arr[low]:
            low = mid + 1
        elif arr[mid] <= arr[high]:
            high = mid - 1
            
n = int(input())
arr = list(map(int, input().split()))
print(arr_min(arr))
