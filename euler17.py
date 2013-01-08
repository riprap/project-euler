"""
If the numbers 1 to 5 are written out in words: one, two,
three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 
letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive
were written out in words, how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342 (three 
hundred and forty-two) contains 23 letters and 115 (one hundred
and fifteen) contains 20 letters. The use of "and" when writing
out numbers is in compliance with British usage.
"""

ones = ["", "one","two","three","four","five","six","seven","eight","nine"]
tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
teens = ["ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"]


def get_ones(number):
	length = len(ones[number])
	return length

def get_teens(number):
	length = len(teens[number])
	return length

def get_tens(number):
	length = len(tens[number])
	return length

def get_letters(number):
	number_string = str(number)
	length = len(number_string)

	if length == 1:
		letters = get_ones(number)

	if length == 2:
		if number >10 and number < 10
	return letters

for i in range(0,10):
	print(get_letters(i))

total_letters = 0

#for i in range (1,1001):
	#total_letters += get_letters(i)