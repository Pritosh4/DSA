'''Given an integer, the task is to write a Python program to convert integer to roman.

Examples:  

Input: 5
Output: V

Input: 9
Output: IX

Input: 40
Output: XL

Input:  1904
Output: MCMIV
Below table shows the list of Roman symbols including their corresponding integer values also:

Symbols	Values
I	1
IV  	4
V	5
IX	9
X	10
XL	40
L	50
XC	90
C	100
CD	400
D	500
CM	900
M	1000'''

def roman(number):
	num = [1, 4, 5, 9, 10, 40, 50, 90,
		100, 400, 500, 900, 1000]
	romans = ["I", "IV", "V", "IX", "X", "XL",
		"L", "XC", "C", "CD", "D", "CM", "M"]
	i = 12
	ans = ''
	while number:
		divide = number // num[i]
		number %= num[i]

		while divide:
			ans += romans[i] 
			divide -= 1
		i -= 1
	return ans


number = int(input())
print(f'The Roman value is:{roman(number)}')
