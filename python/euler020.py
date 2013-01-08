"""n! means n x (n - 1) x ... x 3 x 2 x 1

For example, 10! = 10 x 9 x ... x 3 x 2 x 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!\ """

total = 1

for factorial in range(1,101):
	total *= factorial

total = str(total)
length = len(total)

sum_digits = 0
for digit in range(0,length):
	sum_digits += int(total[digit])
print(sum_digits)