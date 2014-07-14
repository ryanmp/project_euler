import math
def main(n): # What is the largest prime factor of the number 600851475143
	
	''' 
	# this method is slower...
	current_sum = n
	prime_factors = []
	for i in range(2,n):
		if current_sum%i == 0:
			current_sum = current_sum/i
			prime_factors.append(i)
	return prime_factors[-1]
	'''

	for i in xrange(2,int(n/2)-1,1):
		if n%i==0:
			if is_prime(n/i):
				return n/i
	return -1

def is_prime(n):
	for i in xrange(2,int(math.sqrt(n))+1):
		if n%i == 0:
			return False
	return True

if __name__ == '__main__':
	import boilerplate, time
	boilerplate.all(time.time(),main(600851475143)) # under 10 seconds... I'll take it
