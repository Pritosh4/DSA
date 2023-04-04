'''Given two integer N ans K, the task is to find sum of modulo K of first N natural numbers i.e 1%K + 2%K + ….. + N%K.
Input Format

First Line Integer N
Second Line Integer K
Constraints

no

Output Format

Integer with sum
Sample Input 0

10
2
Sample Output 0

5
Explanation 0

Sum = 1%2 + 2%2 + 3%2 + 4%2 + 5%2 + 6%2 + 7%2 + 8%2 + 9%2 + 10%2 = 1 + 0 + 1 + 0 + 1 + 0 + 1 + 0 + 1 + 0 = 5.

Sample Input 1

20
2
Sample Output 1

10'''

n = int(input())
k = int(input())
total = 0
for i in range(1, n + 1):
    total += i % k
    
print(total)
