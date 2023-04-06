'''For a given number find the square root using log function. Number may be int, float or double.

Input Format

Number N
Constraints

no

Output Format

Square root of that number
Sample Input 0

9
Sample Output 0

3.0000000000000004
Sample Input 1

2.93
Sample Output 1

1.711724276862369'''

import math
def root(n):
    return pow(2, 0.5 * (math.log(n))/ math.log(2))

n = float(input())
print(root(n))
