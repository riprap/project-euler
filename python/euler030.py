"""
Find the sum of all the numbers that can be written as 
the sum of fifth powers of their digits.
"""

import math


def keep_going(length):
	total = 0
	placeholder_num = ""
	for i in range(0,length):
		total += math.pow(9,5)
		placeholder_num += "9"
	
	if total < int(placeholder_num):
		return False
	else:
		return True


answer = 0

for num in range (2,9999999):
	num_str = str(num)
	length = len(num_str)
	total = 0
	if length > 10:
		if keep_going(length) == False:
			break

	for digit in range (0,length):
		total += math.pow(int(num_str[digit]), 5) #break num up by digit
	
	if total == num:
		answer += total
		print(total, answer)

print(answer)