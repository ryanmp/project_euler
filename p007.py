import math

def main(n): #What is the 10 001st prime number?
	s = [] # list of primes to be used by our sieve
	nth_prime = len(s)
	i = 1
	while nth_prime<n:
		if not sieved(i,s):
			if is_prime(i):
				nth_prime += 1
				s.append(i)
		i += 1
	i -= 1
	return i

def is_prime(n):
	for i in xrange(2,int(math.sqrt(n))):
		if n%i == 0:
			return False
	return True

def sieved(n,s):
	for i in s:
		if n%i == 0: return True
	return False

if __name__ == '__main__':
	import boilerplate, time, resource
	t = time.time()
	r = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
	boilerplate.all(main(10001), t, r)
