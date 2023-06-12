# Given a number n as a number on a board, find the number of ways the board can be cut so that the resulting number is divisible by 7. 
# 0 is considered divisible by 7 but the number that has a leading 0 cannot be counted. (examples - 070 is considered not divisible by 7)
# Example 1
# Input: 7077
# Output: 8
# The board containing 7077 can be cut into 7,0,7,7,70,07,77,707,077,7077 hence the number of these that are exactly divisble by 7 is 8.
# Input: 5678
# Output: 3
# The board containing 5678 can be cut into 5,6,7,8,56,67,78,567,678 hence the number of these that are exactly divisble by 7 is 3.

n = input()
count = 0
for i in range(1, len(n) + 1):
	for j in range(len(n) - i + 1):
		if int(n[j : j + i]) % 7 == 0:
			count += 1
			if n[j] == '0' and len(n[j : j + i]) > 1:
				count -= 1
print(count)
