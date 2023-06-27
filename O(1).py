'''
Find the sum of numbers that are a multiple of both 3 and 5 for a given range. Solve the problem in a O(1) time complexity
'''

start = int(input())
end = int(input())
lo = start // 15
hi = end // 15
sum_lo = 15 * lo * (lo + 1) / 2
sum_hi = 15 * hi * (hi + 1) / 2
print(sum_hi - sum_lo)
