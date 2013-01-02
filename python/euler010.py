"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
""" 

#passed a number, now check if it's prime ()
def is_prime(number):
	prime = 1
	for a in range(2,int(number/2+1)):
		if number%a == 0:
			prime = 0
			break;
	return prime

total = 0
for number in range(2,2000000):
	if number%50000 == 0:
		print(number)
	if is_prime(number):
		total += number

print(total)