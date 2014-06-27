def main(n): # First triangle number to have over five hundred divisors?
	i = 0; x = 0
	while (True):
		x += 1; i += x
		how_many_divisors = 0
		for j in xrange(1,i+1):
			if i%j==0: #is a divisor
				how_many_divisors += 1
		if how_many_divisors > n:
			return i

if __name__ == '__main__':
	import boilerplate, time
	boilerplate.all(time.time(),main(150)) #this solutions is too slow for n = 500 !