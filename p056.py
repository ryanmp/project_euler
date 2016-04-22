'''

A googol (10^100) is a massive number: one followed by one-hundred zeros;
100^100 is almost unimaginably large: one followed by two-hundred zeros.
Despite their size, the sum of the digits in each number is only 1.

Considering natural numbers of the form, ab, where a, b < 100, what is the maximum digital sum?

'''

def main():
	n = 100
	maximum_digit_sum = 0
	for a in xrange(n):
		for b in xrange(n):
			new_sum = digit_sum(a**b)
			maximum_digit_sum = max(new_sum, maximum_digit_sum)
	return maximum_digit_sum

# in: an integer n
# out: the sum of the digits in n
# since Python supports arbitrarily large Ints, we should be just fine
def digit_sum(n):
	return sum([int(i) for i in list(str(n))])

if __name__ == '__main__':
	import boilerplate, time, resource
	t = time.time()
	r = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
	boilerplate.all(main(), t, r)
