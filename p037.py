'''

The number 3797 has an interesting property.
Being prime itself, it is possible to continuously remove digits from left to right,
and remain prime at each stage: 3797, 797, 97, and 7.
Similarly we can work from right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.

'''

import math
import numpy as np

def is_truncable_prime(n):
	s = str(n)
	for i in xrange(1,len(s)):
		if not is_prime(int(s[i:])):
			return False
	for i in xrange(0,len(s)-1):
		if not is_prime(int(s[:i+1])):
			return False
	return True

def main():
	t_primes = []
	primes = primesfrom2to(750000)
	for p in primes:
		if is_truncable_prime(p):
			t_primes.append(p)

	t_primes = t_primes[4:] # removing 2, 3, 5, 7
	if len(t_primes) == 11:
		return sum(t_primes[4:])

def is_prime(n):
	if n == 1:
		return False

	for i in xrange(2,int(math.sqrt(n))+1):
		if n%i == 0:
			return False
	return True

def primesfrom2to(n):
    # http://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188
    """ Input n>=6, Returns a array of primes, 2 <= p < n """
    sieve = np.ones(n/3 + (n%6==2), dtype=np.bool)
    sieve[0] = False
    for i in xrange(int(n**0.5)/3+1):
        if sieve[i]:
            k=3*i+1|1
            sieve[      ((k*k)/3)      ::2*k] = False
            sieve[(k*k+4*k-2*k*(i&1))/3::2*k] = False
    return np.r_[2,3,((3*np.nonzero(sieve)[0]+1)|1)]


if __name__ == '__main__':
	import boilerplate, time, resource
	t = time.time()
	r = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
	boilerplate.all(main(), t, r)
