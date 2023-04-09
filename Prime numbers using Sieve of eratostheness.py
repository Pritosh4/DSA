'''Given a number n, print all primes smaller than or equal to n. It is also given that n is a small number.
For example, if n is 10, the output should be “2, 3, 5, 7”. If n is 20, the output should be “2, 3, 5, 7, 11, 13, 17, 19”.
Input Format

Integer N
Constraints

no
Output Format

Print all primes smaller than or equal to n.
Sample Input 0

30
Sample Output 0

2 3 5 7 11 13 17 19 23 29
Sample Input 1

5
Sample Output 1

2 3 5'''

def sieve(n):
    prime = [True for i in range(n+1)]
    p = 2
    while p * p <= n:
        if prime[p] == True:
            for i in range(p*p, n+1, p):
                prime[i] = False
        p += 1
    
    for i in range(2, len(prime)):
        if prime[i] == True:
            print(i, end=' ')
    
n = int(input())
sieve(n)
