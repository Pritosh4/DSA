'''Write a program to calculate the value of nCr.

Input Format

First Integer N
Second Integer R
Constraints

no

Output Format

Value of nCr

Sample Input 0

5
2
Sample Output 0

10
Sample Input 1

3
1
Sample Output 1

3'''

def fact(n):
    if n == 0:
        return 1
    return n * fact(n-1)

n = int(input())
r = int(input())
ans = fact(n) / (fact(n-r) * fact(r))
print(int(ans))
