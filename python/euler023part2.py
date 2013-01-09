#euler023part2.py
abundants = []
f = open("abundants.txt",'r')
index = 1
for line in f:
	abundants.append(int(line.replace('\n', '')))

abundant_sums = []
for number1 in abundants:
	if number1 > 14062:
		break
	else:
		for number2 in abundants:
			if (number1 + number2) > 28123:
				break
			else:
				abundant_sums.append(number1+number2)

abundant_sums = list(set(abundant_sums))
abs_sum=0
for i in range (1,28124):
	if i not in abundant_sums:
		abs_sum+=i

print(abs_sum)