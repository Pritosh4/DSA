'''Given two strings s and t, determine if they are isomorphic.
Two strings s and t are isomorphic if the characters in s can be replaced to get t.
All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.
Input Format

First Line string 1
Second Line string 2
Constraints

1 <= s.length <= 5 * 104
t.length == s.length
Output Format

true or false
Sample Input 0

egg
add
Sample Output 0

true
Sample Input 1

foo
bar
Sample Output 1

false'''

def convert(word):
    index_map = {}
    new_str = []
    for i, c in enumerate(word):
        if c not in index_map:
            index_map[c] = i
        new_str.append(str(index_map[c]))
    return ' '.join(new_str)

def isomorphic(s, t):
    return convert(s) == convert(t)

s = input()
t = input()
if isomorphic(s, t) is True:
    print('true')
else:
    print('false')
