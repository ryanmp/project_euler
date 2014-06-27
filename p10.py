def main(n): #returns sum of primes (ex n->2,000,000 = ???)
	primes = []
	for i in xrange(2,n):
		if is_prime(i,primes):
			primes.append(i)
	return sum(primes)	

def is_prime(n,p): #pretty slow
	factors = 0
	for i in p:
		if n%i == 0: return False
	return True

if __name__ == '__main__':
	import boilerplate, time
	boilerplate.all(time.time(),main(200000)) 