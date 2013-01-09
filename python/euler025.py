"""
The Fibonacci sequence is defined by the recurrence 
relation:

Fn = Fn1 + Fn2, where F1 = 1 and F2 = 1.
The 12th term, F12, is the first term to contain three 
digits.

What is the first term in the Fibonacci sequence to 
contain 1000 digits?
"""

f = [0,1,1,2,3,5,8,13,21,34,55,89]

while len(str(max(f))) < 1000:
	f.append(f[-1] + f[-2])
print(f.index(max(f)))