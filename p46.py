'''
What is the smallest odd composite that cannot be written
as the sum of a prime and twice a square?
'''
import math
import numpy as np

def main(m):

	ps = primesfrom2to(m)
	sqrs = [i**2 for i in xrange(1,int(math.sqrt(m)))]

	for i in xrange(5,m,2):

		# just dealing with composites
		if not is_prime(i): 
		#if i not in ps: #slower... but what if I used a set?

			# can we find a prime+sqrt that equals it?
			found_one = False
			for p in ps:
				for sqr in sqrs:
					if i == p + sqr:
						found_one = True

			if not found_one:
				return i
		
	return "no solution in range"


def is_prime(n):
	for i in xrange(3,int(math.sqrt(n))):
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
	import boilerplate, time
	boilerplate.all(time.time(),main(1000)) #looking in range 5 through main(n)