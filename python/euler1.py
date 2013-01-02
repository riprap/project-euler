i = 1
answer=0
while i<1000:
	multiple3 = i%3
	multiple5 = i%5
	if multiple3 == 0 or multiple5 == 0:
		answer += i
		print(i)
	i+=1
print(answer)