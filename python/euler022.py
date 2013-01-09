"""Using names.txt (right click and 'Save Link/Target 
As...'), a 46K text file containing over five-thousand 
first names, begin by sorting it into alphabetical 
order. Then working out the alphabetical value for each 
name, multiply this value by its alphabetical position 
in the list to obtain a name score.

For example, when the list is sorted into alphabetical 
order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, 
is the 938th name in the list. So, COLIN would obtain 
a score of 938 x 53 = 49714.

What is the total of all the name scores in the file?
"""

f = open('names.txt', 'r')
for line in f:
	names = line.replace('"','').split(',')
names.sort()

letters=[]
for i in range (int(ord('A')), int(ord('Z')+1)):
	letters.append(chr(i))


def name_score(name):
	score = 0
	for letter in range(0,len(name)):
		letter_index = int(letters.index(name[letter])) + 1
		score += letter_index
	return score

index = 1
total = 0
for name in names:
	ns = name_score(name)
	total += ns * index
	index += 1 #add one to index
print(total)