'''Catalan numbers are defined as a mathematical sequence that consists of positive integers, which can be used to find the number of possibilities of various combinations.
The nth term in the sequence denoted Cn, is found in the following formula: factorial(2n)/(factorial(n+1) * factorial(n))
The first few Catalan numbers for n = 0, 1, 2, 3, … are : 1, 1, 2, 5, 14, 42, 132, 429, 1430, 4862, …
Input Format

Integer N

Constraints

no

Output Format

Catalan number

Sample Input 0

5
Sample Output 0

42
Sample Input 1

1
Sample Output 1

1'''

def fact(n):
    if n == 0:
        return 1
    return n * fact(n - 1)

n = int(input())
Cn = fact(2 * n)/(fact(n + 1) * fact(n))
print(int(Cn))
