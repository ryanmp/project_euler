'''

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?

'''

import math

def main(n): 
	nth_prime = 0
	i = 1
	while nth_prime<n:
		if is_prime(i):
			nth_prime += 1
		i += 2
	return i - 2

def is_prime(n):
	for i in xrange(2,int(math.sqrt(n)+1)):
		if n%i == 0:
			return False
	return True

if __name__ == '__main__':
	import boilerplate, time, resource
	t = time.time()
	r = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
	boilerplate.all(main(10001), t, r)
