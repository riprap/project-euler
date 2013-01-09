"""
A unit fraction contains 1 in the numerator. The
decimal representation of the unit fractions with
denominators 2 to 10 are given:

1/2	= 	0.5
1/3	= 	0.(3)
1/4	= 	0.25
1/5	= 	0.2
1/6	= 	0.1(6)
1/7	= 	0.(142857)
1/8	= 	0.125
1/9	= 	0.(1)
1/10	= 	0.1
Where 0.1(6) means 0.166666..., and has a 1-digit 
recurring cycle. It can be seen that 1/7 has a 6-digit
recurring cycle.

Find the value of d  1000 for which 1/d contains the 
longest recurring cycle in its decimal fraction part.
"""
from decimal import *
getcontext().prec = 200
def get_decimals():
	decimals = []
	for i in range(2,1000):
		decimals.append(Decimal(1/i))
	return decimals

for decimal in get_decimals():
	dec_str = str(decimal)
	if len(dec_str) < 19:
		continue
	else: #these are the ones with potential repeating
		print(dec_str[2:])