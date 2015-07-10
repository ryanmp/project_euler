'''

The smallest number expressible as the sum of a prime square,
prime cube, and prime fourth power is 28. In fact, there are
exactly four numbers below fifty that can be expressed in such a way:

28 = 2^2 + 2^3 + 2^4
33 = 3^2 + 2^3 + 2^4
49 = 5^2 + 2^3 + 2^4
47 = 2^2 + 3^3 + 2^4

How many numbers below fifty million can be expressed as the
sum of a prime square, prime cube, and prime fourth power?

'''

import math
import numpy as np

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

def main():	
	max_n = int(50e6)
	max_2 = int(math.ceil(math.pow(max_n,1./2)))
	max_3 = int(math.ceil(math.pow(max_n,1./3)))
	max_4 = int(math.ceil(math.pow(max_n,1./4)))

	all_primes = primesfrom2to(max_2)
	primes_2, primes_3, primes_4 = [], [], []
	for p in all_primes:
		if p <= max_2:
			primes_2.append(p)
		if p <= max_3:
			primes_3.append(p)
		if p <= max_4:
			primes_4.append(p)

	all_solutions = set()

	for p2 in primes_2:
		for p3 in primes_3:
			for p4 in primes_4:
				ans = p2**2 + p3**3 + p4**4
				if ans < max_n:
					all_solutions.add(ans)

	return len(all_solutions)

if __name__ == '__main__':
	import boilerplate, time
	boilerplate.all(time.time(),main())
	

