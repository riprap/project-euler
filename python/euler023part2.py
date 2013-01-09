#euler023part2.py
abundants = []
f = open("abundants.txt",'r')
index = 1
for line in f:
	abundants.append(int(line.replace('\n', '')))

abundant_sums = []
for number1 in abundants:
	for number2 in abundants:
		abundant_sums.append(number1 + number2)

print(abundant_sums[0:10])