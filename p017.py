'''

If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there
are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words,
how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two)
contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and"
when writing out numbers is in compliance with British usage.

'''

d = {1:3, 2:3, 3:5, 4:4, 5:4, 6:3, 7:5, 8:5, 9:4, 10:3, 11:6, 12:6, 13:8, 14:8, 15:7,
	16:7, 17:9, 18:8, 19:8, 20:6, 30:6, 40:5, 50:5, 60:6, 70:7, 80:6, 90:6}

def main():

	n = 1000
	# don't forget 'hundred' & 'and' (...that'll be in the conditional logic)

	total_count = 0
	for i in xrange(1,n+1):	
		total_count += get_char_cnt(i)

	return total_count


def get_char_cnt(i):

	if (i < 1 or i > 1000):
		print "number range error: n must be in the range 1:1000"

	count = 0
	if (i == 1000):
		count += 11

	if (i>=100 and i<1000):
		dig1 = (i/100)
		count += d[dig1] + 7 # 7=hundred
		i = i%100
		if i != 0:
			count += 3 # 3=and

	if (i<100 and i>=20):
		dig1 = (i/10)*10
		count += d[dig1]
		i = i%10

	if (i>0 and i<20):
		count += d[i]

	return count

if __name__ == '__main__':
	import boilerplate, time, resource
	t = time.time()
	r = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
	boilerplate.all(main(), t, r)


