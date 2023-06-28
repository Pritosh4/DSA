'''
We have an infinite no. of Rs. 1, Rs. 2, and Rs. 5 coins. Pick the number of coins such that the sum of denominations of the picked coins is n
and the coins can denote any value from 1 to n.
Do in O(1)

Eg: n = 13
5  2  1
2  1  1 --> Though 5 + 5 + 2 + 1 = 13 but this is not the answer as this combination cannot denote 4.

5  2  1
1  3  2 --> Though 5 + 2 + 2 + 2 + 1 + 1 and all denominations from 1 to 13 can be denoted 

'''

n = int(input())
five = (n - 4) // 5
n = n - (five * 5)
if n % 2 == 0:
	one = 2
else:
	one = 1
n = n - (one * 1)
two = n // 2
print(five, two, one)

'''
Once we have sufficient 5s to get upto the value of n - 5. We then only need to worry about getting the additional 1s and 2s to get the exact answer of n.
if n is even we need 2 ones else we only need 1 one and the rest can be the twos
'''
