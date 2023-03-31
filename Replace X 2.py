'''Given a string, compute recursively a new string where all 'x' chars have been removed.

Input Format

String S

Constraints

1 <= |S| <= 10^3 where |S| represents the length of string S.

Output Format

Modified string

Sample Input 0

xaxb
Sample Output 0

ab
Sample Input 1

abc
Sample Output 1

abc'''

def remove_x(word):
    if len(word) == 0:
        return ''
    if word[0] == 'x':
        return remove_x(word[1:])
    return word[0] + remove_x(word[1:])
    

word = input()
print(remove_x(word))
