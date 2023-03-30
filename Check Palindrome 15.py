'''Check whether a given String S is a palindrome using recursion. Return true or false.

Input Format

String S

Constraints

0 <= |S| <= 1000
where |S| represents length of string S.
Output Format

true or false

Sample Input 0

racecar
Sample Output 0

true
Sample Input 1

face
Sample Output 1

false'''

def check(word):
    if len(word) < 1:
        return True
    if word[0] == word[-1]:
        return check(word[1:-1])
    else:
        return False


word = input()
if check(word) is True:
    print('true')
else:
    print('false')
