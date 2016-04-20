'''

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

'''

from datetime import date, timedelta

# let's just use datetime...
def main():
	start_dt = date(1901, 1, 1)
	end_dt = date(2001, 1, 1)
	
	sundays = 0
	for single_date in daterange(start_dt, end_dt):
		if single_date.weekday() == 6:
			sundays += 1 

	return sundays
    
def daterange(start_date, end_date):
	    for n in range(int((end_date - start_date).days)):
	        yield start_date + timedelta(n)

if __name__ == '__main__':
	import boilerplate, time, resource
	t = time.time()
	r = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
	boilerplate.all(main(), t, r)
