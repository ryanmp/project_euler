import numpy as np
from collections import deque
def main(n): # how many circular primes below 1 mil?
	
	primes = set(primesfrom2to(n)) # all normal primes
	c_primes = []

	for i in primes:
		l = deque(str(i))
		rotations = [] # create a list of rotations
		for i in xrange(len(l)):
			as_string = ''.join(l)
			rotations.append(int(as_string))
			l.rotate()

		is_c_prime = True
		for i in rotations:
			if i not in primes: # are all rotations prime?
				is_c_prime = False
				break
		if (is_c_prime):
			c_primes.append(i)

	return len(c_primes) # how many c_primes
		

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
	boilerplate.all(time.time(),main(1000000))
