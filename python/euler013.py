"""
Work out the first ten digits of the sum of the following 
one-hundred 50-digit numbers (found in euler013.txt)
"""

f = open('euler013.txt', 'r')
for line in f:
	total += int(line)
total_string = str(total)
print (total_string[:10])
