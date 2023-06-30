'''
Count the number of set bits of n. The loop should only run for the number of 1s there are in n.
'''
n = int(input())
count = 0
while n != 0:
    n = n & (n-1)
    count += 1
print(count)
