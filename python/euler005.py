"""
2520 is the smallest number that can be divided by each
of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly
divisible by all of the numbers from 1 to 20?
"""

#loop through increasing numbers
for number in range(20,1000000000,20):
	divisible = 1
	for divider in range (1,21):
		if number%divider != 0:
			divisible = 0
			break;
	if divisible:
		print (number)
		break;

#check if number is divisible from 1-20
#loop through 1 to 20
#if first counter modulo second counter != 0 break
#if not found, print "$first_counter" is the smallest number