'''
Given n no. of coins with denominations 1 to n, find the minimum no. of coins hat you need to get all the denomination values.
Each coin can only be used once
'''
n = int(input())
count = 0
while n != 0:
	count += 1
	n = n >> 1
print(count)

'''
n = 10
1 2 3 4 5 6 7 8 9 10
pick 1
pick 2
3 possible using 1 + 2 so we don't pick 3
pick 4
5 possible using 1 + 4 so we don't pick 5
6 possible using 4 + 2 so we don't pick 6
7 possible using 1 + 2 + 4 so we don't pick 7
pick 8 
9 possible using 1 + 8 so we don't pick 9
10 possible using 8 + 2 so we don't pick 10
Thus the coins we need are
1 2 4 8
which are basically the powers of 2



'''
