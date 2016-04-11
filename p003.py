'''

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

'''

import math

def factors(n):    
	return reduce(list.__add__, 
		([i, n//i] for i in range(1, int(math.sqrt(n)) + 1) if n % i == 0))

def is_prime(n):
	for i in xrange(2,int(math.sqrt(n))+1):
		if n%i == 0:
			return False
	return True

def main(n): 
	factor_list = factors(n)
	factor_list.sort(reverse=True)
	for i in factor_list:
		if is_prime(i):
			return i
	return -1

if __name__ == '__main__':
	import boilerplate, time, resource
	t = time.time()
	r = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
	boilerplate.all(main(600851475143), t, r)
