'''

The first two consecutive numbers to have two distinct prime factors are:

14 = 2 x 7
15 = 3 x 5

The first three consecutive numbers to have three distinct prime factors are:

644 = 2^2 x 7 x 23
645 = 3 x 5 x 43
646 = 2 x 17 x 19.

Find the first four consecutive integers to have four distinct prime factors. What is the first of these numbers?

'''

from math import sqrt


def is_prime(n):
	if n == 1:
		return False
	for i in xrange(2,int(math.sqrt(n))+1):
		if n%i == 0:
			return False
	return True


def count_prime_factors(n):

	results = set()
	for i in xrange(1, int(math.sqrt(n)) + 1):
		if n % i == 0:
			if is_prime(i):
				results.add(i)
			if is_prime(int(n/i)):
				results.add(int(n/i))
	return len(results)


def main():
	# find sequence
	n = 4
	seq_count = 0
	i = 210
	while (True):
		i += 1
		if count_prime_factors(i) == n:
			seq_count += 1
		else:
			seq_count = 0

		if seq_count == n:
			return i-n+1
			break



if __name__ == '__main__':
	import boilerplate, time, resource
	t = time.time()
	r = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
	boilerplate.all(main(), t, r) # this feels slow... but maybe this is the best I can do for now?



