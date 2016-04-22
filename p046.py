'''

It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.

9 = 7 + 2x1^2
15 = 7 + 2x2^2
21 = 3 + 2x3^2
25 = 7 + 2x3^2
27 = 19 + 2x2^2
33 = 31 + 2x1^2

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?

'''
import math

def main():

	# picking an arbitrary test set for our primes & twice_a_sqrs
	# if our solution is larger than this value, we could have a problem (will need to increase it's size)
	m = 10000
	ps = primesfrom2to(m)
	sqrs = [2*i**2 for i in xrange(1,int(math.sqrt(m)))]

	i = 5
	while(True):

		if not is_prime(i): # just dealing with composites

			# can we find a prime+sqrt that equals it?
			found_one = False
			for p in ps:
				if p > i:
					break
				for sqr in sqrs:
					if sqr > i:
						break
					if i == p + sqr:
						found_one = True

			if not found_one:
				return i
		
		i += 2 # working our way up through all odd numbers

	return "no solution in range"

def is_prime(n):
	for i in xrange(3,int(math.sqrt(n))):
		if n%i == 0:
			return False
	return True

def primesfrom2to(n):
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
