# How many n-digit positive integers exist which are also an nth power?
def main(n):
	count = 0
	for i in xrange(1,n):
		if has_nth_power(i):
			count += 1

	return count

def digit_count(n):
	return len(str(n))

def has_nth_power(n):
	digits = digit_count(n)
	base = 2
	while(True):
		val = base**digits
		if val == n:
			return True
		elif val > n:
			return False
		else:
			base += 1

if __name__ == '__main__':
	import boilerplate, time
	# how do we determine the upper limit for n?
	boilerplate.all(time.time(),main(100000)) 