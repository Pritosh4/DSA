'''Given a number n, write an efficient function to print all prime factors of n. For example, if the input number is 12, then the output should be “2 2 3”. And if the input number is 315, then the output should be “3 3 5 7”.

Input Format

Integer N

Constraints

No

Output Format

Prime factors of that integer

Sample Input 0

12
Sample Output 0

2 2 3
Sample Input 1

315
Sample Output 1

3 3 5 7'''

n = int(input())
while n % 2 == 0:
    n /=  2
    print(2, end = ' ')
for i in range(3, int(pow(n, 0.5)) + 1, 2):
    while n % i == 0:
        print(i, end = ' ')
        n /= i

if n > 2:
    print(int(n), end = ' ')
