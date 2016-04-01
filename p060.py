'''
The primes 3, 7, 109, and 673, are quite remarkable.
By taking any two primes and concatenating them in any order the result will always be prime.
For example, taking 7 and 109, both 7109 and 1097 are prime.
The sum of these four primes, 792, represents the lowest sum for a set of four primes with this property.

Find the lowest sum for a set of five primes for which any two primes concatenate to produce another prime.


'''

import math
import numpy as np
import itertools

def is_prime(n):
	for i in xrange(2,int(math.sqrt(n))+1):
		if n%i == 0:
			return False
	return True

def are_all_prime(ls):
	for x in ls:
		if not is_prime(x):
			return False
	return True

def concat(a,b):
	return int(str(a) + str(b))

def any_two_concats(ls):
	ret = []
	combos = list(itertools.combinations(ls,2))
	for c in combos:
		ret.append(concat(c[0],c[1]))
		ret.append(concat(c[1],c[0]))
	return ret

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




'''
hm.... the following exhaustive approach (using all combinations) is going to be way too slow. Will need to look for substantial improvements
when I revisit this problem.
'''


primes_list = primesfrom2to(100)
print "testing first",len(primes_list),"primes - largest <",max(primes_list)

xs = itertools.combinations(primes_list, 4)

for x in xs:
	concats = any_two_concats(x)
	if are_all_prime(concats):
		print x, concats
		






















