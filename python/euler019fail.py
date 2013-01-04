
"""
Gave up and tried another method

You are given the following information, but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

"""
#we do not have to worry about below since 2000 is divisible by 400
#A leap year occurs on any year evenly divisible by 4, 
#but not on a century unless it is divisible by 400.

#January 1, 1900 was a Monday (day 2)
year = 1900
month = 1
day = 2

#Start on January 1, 1901 (365 days since 1900 wasnt leap year)
day += 365%7
year += 1
total=0

#if adds 31 days, day += 3
#if month>12:
#	month = 1
#	year+=1
for year in range (1900,2001):
	for month in range (1,13):
		if month in [4,6,9,11]:
			days = 30

		elif month == 2:
			if year%4 == 0:
				days = 29
			#day can remain the same since the 1st will be the same day the following month

		else:
			days = 31

		day += days%7
		if day>7:
			day -= 7

		if day == 1:
			total += 1
			#print( day,month,year)

print(total)