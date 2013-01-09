"""
Let d(n) be defined as the sum of proper divisors of 
n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a != b, then a and b 
are an amicable pair and each of a and b are called 
amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 
5, 10, 11, 20, 22, 44, 55 and 110; therefore 
d(220) = 284. The proper divisors of 284 are 1, 2, 4, 
71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers < 10000
"""


def get_divisors(number):
	factors = []
	end = number
	for x in range(1, end):
		if number%x == 0:
			factors.append(x)
	return factors

total = 0
amicable = []
for a in range(1,10000):
	if a in amicable:
		continue
	b = 0
	number1 = get_divisors(a)
	for number in number1:
		b += number

	new_a = 0
	number2 = get_divisors(b)
	for number in number2:
		new_a += number

	if new_a == a and a!=b:
		total += a
		total += b
		amicable.append(b)
		print("Amicable:",a,b)

print(total)
"""
total = 0
for number1 in range(1,10000):
	print(number1)
	divisors_sum = 0
	divisors = get_divisors(number1)
	for divisor in divisors:
		divisors_sum += divisor
	number2 = divisors_sum
	divisors_sum = 0
	divisors = get_divisors(number2)
	for divisor in divisors:
		divisors_sum += divisor
	if divisors_sum == number2 and number1 != number2:
		total+= divisors_sum
		print("Amicable: %s\nTotal: %s"%(divisors_sum, total))

print ("Sum:", total)
"""