'''

The prime 41, can be written as the sum of six consecutive primes:

41 = 2 + 3 + 5 + 7 + 11 + 13
This is the longest sum of consecutive primes that adds to a prime below one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most consecutive primes?

'''

import numpy as np
import math

def is_prime(n):
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



def main():


	'''

	this current method doesn't quite work yet.... it's just going to be too slow to check all the possibilities


	'''

	primes = primesfrom2to(1000000)
	#print len(primes)

	which_prime = 0
	biggest_chain_len = 0


	found_one = True

	for chain_len in xrange(75,100):

		for i in xrange(0,len(primes)-chain_len):
			chain = primes[i:i+chain_len]

			if is_prime(sum(chain)):
				
				biggest_chain_len = chain_len
				which_prime = sum(chain)
				print "length of chain:", biggest_chain_len, "prime:", which_prime
				break



