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
	factors = 0
	for i in xrange(1,n+1):
		if n%i == 0: factors += 1
	if factors == 2: return True
	else: return False 

def sieved(n,s):
	for i in s:
		if n%i == 0: return True
	return False

if __name__ == '__main__':
	import boilerplate, time
	boilerplate.all(time.time(),main(10001))
