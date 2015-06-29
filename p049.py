import numpy as np
from itertools import permutations
def main():
	# find a sequence of 3, four-digit primes with a few properties:
	#	+ forms a arithmatic sequence
	#	+ all three are permutations of each other
	
	# generate a list of all 4-digit primes
	primes_list = list(primesfrom2to(9876))
	start_idx = primes_list.index(1009)-1
	primes_list = primes_list[start_idx:] 

	# just for testing, let's verify that this prime works
	this_prime = 1487

	# all permutations of a given prime
	l = list(permutations(list(str(this_prime))))
	list_of_perms = set()
	for tup in l:
		temp_perm = int(''.join(str(i) for i in tup))
		list_of_perms.add(temp_perm)

	# reduce to only permutations which are prime
	matches = []
	for i in list_of_perms:
		for j in primes_list:
			if i == j:
				matches.append(i)
	matches.sort()
	
	# calculate all possible differences (a - b) to find 
	# an arithmatic sequence
	diffs = []
	for i in matches:
		for j in matches:
			diff = j - i
			if diff > 0:
				diffs.append((diff,i,j))


	''' whew... getting there slowly but surely. I thought this problem would 
	be nice and simple. Perhaps I am overcomplicating it....'''
	print diffs
	return 0

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
	boilerplate.all(time.time(),main())
