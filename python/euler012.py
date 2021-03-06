"""
The sequence of triangle numbers is generated by adding the natural numbers. 
So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. 
The first ten terms would be:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

Let us list the factors of the first seven triangle numbers:

 1: 1
 3: 1,3
 6: 1,2,3,6
10: 1,2,5,10
15: 1,3,5,15
21: 1,3,7,21
28: 1,2,4,7,14,28
We can see that 28 is the first triangle number to have over five divisors.

What is the value of the first triangle number to have over five hundred divisors?
"""


def get_factors(number):
	factors = []
	end = number+1
	for x in range(1, end):
		if number%x == 0:
			factors.append(x)
	return factors


"""
An idea would be to only add the next number to the previous number... 
This would improve perforamnce
"""
run = True
number = 1
count = 1
previous_factors = 1
while True:
	count+=1
	number += count
	factors = len(get_factors(number))
	if factors > previous_factors:
		print(factors)
		previous_factors = factors
	if factors >= 500:
		print ("Triangular number: %s\nCount: %s\nFactors: %s"%(number,count, factors))
		break
