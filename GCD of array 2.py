'''Given an array of numbers, find GCD of the array elements

Input Format

First Line array size
Second Line array elements
Constraints

No
Output Format

GCD of elements of array
Sample Input 0

5
2 4 6 8 16
Sample Output 0

2
Sample Input 1

3
1 2 3
Sample Output 1

1'''

def getGCD(a, b):
    while(a > 0 and b > 0):
        if(a > b):
            a = a % b
        else:
            b = b % a
            
    if(a == 0):
        return b
    
    return a


def GcdOfArray(arr):
    gcd = 0
    for i in range(len(arr)):
        gcd = getGCD(gcd, arr[i])
    return gcd



n = int(input())
arr = list(map(int, input().split()))
print(GcdOfArray(arr))

