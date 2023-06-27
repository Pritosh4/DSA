'''
Print factors of a given number in sorted order. Solve with a time complexity og O(sqrt(n))
'''
n = int(input())
stack = []
i = 1
while i*i <= n:
	if n % i == 0:
		if n / i == i:
			print(i)
		else:
			print(i)
			stack.append(n // i)
	i += 1

while stack:
	print(stack.pop())
