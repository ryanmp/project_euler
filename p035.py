'''

The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100:
2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?

'''

from collections import deque

def main(): # how many circular primes below 1 mil?
	
	n = 1000000
	primes = set(primes_list(n)) # all normal primes
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
		
def primes_list(n):
     # http://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188
    """ Returns  a list of primes < n """
    sieve = [True] * n
    for i in xrange(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)/(2*i)+1)
    return [2] + [i for i in xrange(3,n,2) if sieve[i]]

if __name__ == '__main__':
	import boilerplate, time, resource
	t = time.time()
	r = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
	boilerplate.all(main(), t, r)



