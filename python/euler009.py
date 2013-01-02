"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
""" 

#Has to be a<b<c so we can try to find combinations using that
#we also need the sum of a + b + c to be 1000

for a in range(1,1001):
	for b in range(a,1001):
		for c in range(b,1001):
			if (a+b+c) == 1000:
				if ((a*a) + (b*b)) == (c*c):
					print (a,b,c)
					print(a*b*c)