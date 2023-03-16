'''Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

Input Format

First line contains the value of size of your array
Line consists of 'n' space seperated integers representing the values present in the Array
Third line having the K value, how much you want to rotate
Constraints

1 <= nums.length <= 10^5
-231 <= nums[i] <= 231 - 1
0 <= k <= 10^5
Output Format

Rotated Array
Sample Input 0

7
1 2 3 4 5 6 7
3
Sample Output 0

5 6 7 1 2 3 4
Explanation 0

rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
Sample Input 1

4
-1 -100 3 99
2
Sample Output 1

3 99 -1 -100
Explanation 1

rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]'''

def reverse(arr, i, j):
    low = i
    high = j
    while low < high:
        arr[low], arr[high] = arr[high], arr[low]
        low += 1
        high -= 1
        
def rotate(arr, k, n):
    k = k % n
    reverse(arr, 0, n - k - 1)
    reverse(arr, n - k, n -1)
    reverse(arr, 0, n - 1)
    
n = int(input())
arr = list(map(int,input().split()))
k = int(input())
rotate(arr, k, n)
for i in arr:
    print(i, end=' ')
