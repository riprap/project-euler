"""
2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?
"""

import math

number = (int(math.pow(2,1000)))
num_string = str(number)
num_length = len(num_string)

total = 0

for i in range(0,num_length):
	total += int(num_string[i])
print(total)