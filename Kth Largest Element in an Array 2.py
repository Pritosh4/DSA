'''Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

Input Format

Value represnting size of your array
Line consists of 'n' space seperated integers representing the values present in the Array
K value
Constraints

1 <= k <= nums.length <= 10^5
Output Format

Kth Largest Element in array

Sample Input 0

8
1 2 3 4 5 6 7 8
2
Sample Output 0

7
Sample Input 1

9
3 2 3 1 2 4 5 5 6
4
Sample Output 1

4'''

n = int(input())
arr = list(map(int, input().split()))
k = int(input())
arr.sort()
print(arr[-k])
