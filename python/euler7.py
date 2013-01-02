"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, 
we can see that the sixth prime is 13.

What is the 10 001st prime number?
"""

#passed a number, now check if it's prime ()
def is_prime(number):
	prime = 1
	for a in range(2,int(number/2+1)):
		if number%a == 0:
			prime = 0
			break;
	return prime


prime_number = 10001
count=1
num = 2
run = True
while run == True:
	if is_prime(num):
		if count == prime_number:
			print ("The %s prime number is %s" % (count, num))
			break;
		count+=1
	if num == 2: #special case to go from 2 to 3
		num+=1
	else:
		num+=2