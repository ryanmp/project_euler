import math
def main(n): # First triangle number to have over five hundred divisors?
	i = 0; x = 0 # lower bound....
	max_divisors = -1
	while (True):
		x += 1; i += x
		how_many_divisors = 0
		for j in xrange(1,int(math.sqrt(i))):
			if i%j==0: #is a divisor
				how_many_divisors += 2 # always in pairs
		max_divisors = max(max_divisors,how_many_divisors)
		if how_many_divisors > n:
			return i

if __name__ == '__main__':
	import boilerplate, time
	boilerplate.all(time.time(),main(500)) # under 10 seconds... good enough