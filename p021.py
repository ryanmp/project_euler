def main(): # Evaluate the sum of all the amicable numbers under 10000

	n = 10000

	amicable_numbers = []
	for i in xrange(1,n):
		a = proper_divisors(i)
		b = proper_divisors(sum(a))
		if sum(b) == i and sum(a) != sum(b):
			amicable_numbers.append(i)
	return sum(amicable_numbers)

def proper_divisors(n):
	ret = []
	for i in xrange(1,int(n/2)+1):
		if n%i == 0:
			ret.append(i)
	return ret

if __name__ == '__main__':
	import boilerplate, time, resource
	t = time.time()
	r = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
	boilerplate.all(main(), t, r)