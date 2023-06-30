'''
Check if a number is a power of 4 or not. Solve in O(1)
'''
n = int(input())
if (n & n-1) == 0:
    if n % 3 == 1:
        print('Yes the number is a power of 4')
else:
    print('No the number is not a power of 4')
