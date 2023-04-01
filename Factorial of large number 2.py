'''Find the factorial of a large number.

Input Format

Integer N

Constraints

No

Output Format

Factorail of the integer

Sample Input 0

100
Sample Output 0

93326215443944152681699238856266700490715968264381621468592963895217599993229915608941463976156518286253697920827223758251185210916864000000000000000000000000
Sample Input 1

50
Sample Output 1

30414093201713378043612608166064768844377641568960512000000000000'''

def fact(n):
    if n == 0:
        return 1
    return n * fact(n - 1)

n = int(input())
print(fact(n))
