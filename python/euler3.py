"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143?
"""

number = 600851475143
#check_primes_below = int(number/2)
#primes = get_primes(check_primes_below)
#answer = get_largest_prime_factor(primes, number)
#print(answer)


#passed a number, now check if it's prime ()
def is_prime(number):
	prime = 1
	for a in range(2,int(number/2+1)):
		if number%a == 0:
			prime = 0
			break;
	return prime


for i in range(2, number):
	if number%i == 0:
		factor = number/i
		print("Checking if %s is prime" %(factor))
		prime = is_prime(factor)
		if prime:
			print ("%s is the largest prime factor!" % factor)
			break;













#Below is what i previously had (made it more complicated than it was)
"""
Start at the number/2 then go down until you find 
the largest factor
"""

"""
@param int number - check to see if this number is prime
"""
def is_prime(number):
	number = maximum/2

	count1 = 2
	while count1 < number:
		count2 = 2
		while count2 < number:
			if count2 * count1 == number:
				run = false
		count1+=1

"""
@param int maximum - find all prime numbers below this maximum
@return list[int] primes_list - returns the list of prime numbers 
                           to be checked for factors
"""
def get_primes(maximum):
	"""
	Ok, how are we going to figure out if its a prime number?
	Hey, I know the answer to this one.
	No two numbers can be multiplied together to form this number!
	Starting at 2*2 then going to 3*2 and 3*3, then 4*2, 4*3, 4*4 etc
	How about we have a number, and then check if any of these combinations 
	make that number, until we are at half that number!
	"""

	primes_list = [2,3] #start with these 2
	number = 4
	while number <= maximum:
		if number%1000 == 0:
			print(number)
		prime = 1 #Will make @var prime False if we find factors for number
		
		for multiple1 in range(2, number):
			for multiple2 in range(2, number):
				if multiple1*multiple2 == number:
					prime = 0
					break;
		if prime:
			primes_list.append(number)
		
		number += 1 #increase our number by 1, then check if that's prime
	return primes_list


"""
@param list[int] primes_list - contains all primes to check
@param int number - check if primes are a factor of this
"""
def get_largest_prime_factor(primes_list, number):
	"""
	Check the largest prime number first
	"""
	primes_list.sort()
	primes_list.reverse()
	for prime in primes_list:
		multiplier = 2
		while multiplier<=(number/2):
			if prime * multiplier == number:
				return prime #this is our largest prime factor!
			multiplier+=1
	

