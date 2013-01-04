"""
You are given the following information, but you may prefer to do some 
research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a 
century unless it is divisible by 400.
How many Sundays fell on the first of the month during the twentieth century 
(1 Jan 1901 to 31 Dec 2000)?
"""

def month_first_days(start,finish):
	first_day_list = []
	day = 1
	for year in range(start,finish):
		for month in range(1,13):
			first_day_list.append(day)
			if month in [4,6,9,11]:
				day+=30
			elif month == 2:
				day+=28
				if year%4 == 0:
					day+=1
				#day can remain the same since the 1st will be the same day the following month
			else:
				day += 31
	return first_day_list

first_days = month_first_days(1901,2001)
#January 1st, 1900 is a Monday.
jan_1_1900 = 1 #Monday, we want a 7 (Sunday)
jan_1_1901 = jan_1_1900+(365%7)  #2 = Tuesday
difference = 7 - jan_1_1901
first_sunday = difference + 1 #add one since we started on the first

total = 0
for a in range (first_sunday,max(first_days)+10,7):
	if a in first_days:
		total += 1
print (total)






"""day = 2  
start_day = day + 365%7 #January 1, 1901 = 3 (Wednesday)
#Ok now what day is the first Sunday on?
#figure out which day after the 1st 
first_sunday = 7 - start_day
print (first_sunday)

for days in first_days:
	print("%s are the first days of each month in the days of the year "%days)"""