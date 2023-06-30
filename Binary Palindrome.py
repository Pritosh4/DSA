'''
Check if the binary representation of n is a palindrome or not without converting the number into its binary form.
'''


n = int(input())
temp = n
rev = 0
while n != 0:
    rev = rev << 1
    if n & 1 == 1:
        rev = rev ^ 1
    n = n >> 1

if temp == rev:
    print('Yes the binary representation of the number is a palindrome')
else:
    print('No the binary representation of the number is not a palindrome ')
