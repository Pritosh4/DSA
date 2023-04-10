'''For a given a string expression containing only round brackets or parentheses, check if they are balanced or not. Brackets are said to be balanced if the bracket which opens last, closes first.

Input Format

Expression: (()())
Since all the opening brackets have their corresponding closing brackets, we say it is balanced and hence the output will be, 'true'.
You need to return a boolean value indicating whether the expression is balanced or not.
Note:
The input expression will not contain spaces in between.
Constraints

1 <= N <= 10^7
Where N is the length of the expression.
Time Limit: 1sec
Output Format

The only line of output prints 'true' or 'false'.
Sample Input 0

(()()())
Sample Output 0

true
Sample Input 1

()()(()
Sample Output 1

false'''

def balance(Exp):
    stack = []
    for i in exp:
        if i == '[' or i == '(' or i =='{':
            stack.append(i)
        elif not stack:
            return False
        elif i == ']':
            top = stack.pop()
            if '[' != top:
                return False
        elif i == ')':
            top = stack.pop()
            if '(' != top:
                return False
        elif i == '}':
            top = stack.pop()
            if '{' != top:
                return False
    if stack:
        return False
    return True

exp = input()
if balance(exp) is True:
    print('true')
else:
    print('false')
        
