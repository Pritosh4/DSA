'''You have been given a sorted(in ascending order) integer array/list(ARR) of size N and an element X. Write a function to search this element in the given input array/list using 'Binary Search'. Return the index of the element in the input array/list. If the element is not present in the array/list, then return -1.

Input Format

Value representing size of the array
Line consists of 'n' space seperated integers representing the values present in the Array
Target Element which we needs to find
Constraints

No

Output Format

Index of that target element

Sample Input 0

3
1 2 3
0
Sample Output 0

-1
Explanation 0

0 is not present in the array, so give -1 as answer'''

def search(arr, n, index):
    low, high = 0, n - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == index:
            return mid
        elif arr[mid] > index:
            high = mid - 1
        else:
            low = mid + 1
    return -1
    


n = int(input())
arr = list(map(int, input().split()))
index = int(input())
print(search(arr, n, index))
