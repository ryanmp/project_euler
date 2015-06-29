'''
We shall say that an n-digit number is pandigital
if it makes use of all the digits 1 to n exactly once.
For example, 2143 is a 4-digit pandigital and is also prime.

Q: What is the largest n-digit pandigital prime that exists?
'''
import numpy as np
def main():
	biggest = 2143
	p = primesfrom2to(9876543)
	print len(primesfrom2to(9876543))
	for i in p:
		if is_pandigital(i):
			biggest = max(biggest, i)
	return biggest


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


def is_pandigital(n):
	l = len(str(n))
	arr = [int(i) for i in list(str(n))]
	arr.sort()
	if arr == [i for i in xrange(1,l+1)]:
		return True
	else:
		return False


# once again... it's too slow. we really don't want to store all the primes before checking
# to see if they are pandigital. solution: combine a prime check with is_pandigital
# how about we try using a generator for our primes, that could be fun...
if __name__ == '__main__':
	import boilerplate, time
	boilerplate.all(time.time(),main())
