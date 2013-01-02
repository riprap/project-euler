"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""
"""
Order I want
999 * 999 -> check if palindrome
999 * 998
998 * 998
998 * 997
997 * 997
997 * 996
"""


def is_palindrome(number):
	num_string = str(number)
	num_length = len(num_string)

	if num_length%2 == 0:
		middle = int(num_length/2)
		rev_num_string = ""
		reverse = range (-1, (middle*(-1)-1), -1)
		
		for i in reverse:
			rev_num_string += num_string[i]
		
		if rev_num_string == num_string[:middle]:
			return True
	
	return False
	#reverse the 2nd part, check is equal to 1st part'
palindromes = []
for a in range(999,99,-1):
	for i in range(a,99,-1):
		number = (a * i)

		if is_palindrome(number):
			palindromes.append(number)

print (max(palindromes))