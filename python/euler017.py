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
	number_string = str(number)
	if number >= 10 and number < 20:
		length = get_teens(int(number_string[1]))
	elif number < 10:
		length = get_ones(number)
	else:
		tens_digit = int(number_string[0])
		length = len(tens[tens_digit])
		ones_digit = int(number_string[1])
		length += get_ones(ones_digit)

	return length

def get_hundreds(number):
	number_string = str(number)
	length = get_ones(int(number_string[0]))
	length +=  len("hundred") #get hundreds length of letters
	
	if number_string[-2:] != '00':
		length += len("and") #add and for all hundreds not ending in 00
		length += get_tens(int(number_string[1:3]))

	return length

def get_letters(number):
	number_string = str(number)
	length = len(number_string)

	if length == 1:
		letters = get_ones(number)

	if length == 2:
		letters = get_tens(number)

	if length == 3:
		letters = get_hundreds(number)

	if length == 4:
		letters = len("onethousand")
		
	return letters

total = 0
for i in range(1,1001):
	total +=  get_letters(i)
print (total)

#total_letters = 0

#for i in range (1,1001):
	#total_letters += get_letters(i)