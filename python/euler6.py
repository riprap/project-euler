"""
The sum of the squares of the first ten natural numbers is,

1^2 + 2^2 + ... + 10^2 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)^2 = 55^2 = 3025
Hence the difference between the sum of the squares of the first ten natural 
numbers and the square of the sum is 3025  385 = 2640.

Find the difference between the sum of the squares of the first one hundred
natural numbers and the square of the sum.
"""

def sum_of_squares():
	total = 0
	for natural in range(1,101):
		total += natural*natural
	return total

def square_of_sum():
	total = 0
	for natural in range(1,101):
		total += natural
	return total * total

difference = square_of_sum() - sum_of_squares()
print (difference)