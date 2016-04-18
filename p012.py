import math
def main(n): # First triangle number to have over five hundred divisors?

	i = 1
	while (True):
		tri_num = tri_number(i)
		how_many_divisors = len(factors(tri_num))
		if how_many_divisors > n:
			return tri_num
		i += 1

def factors(n):    
	return reduce(list.__add__, 
		([i, n//i] for i in range(1, int(math.sqrt(n)) + 1) if n % i == 0))


def tri_number(n):
	return int(n*(n+1)/2.0)

if __name__ == '__main__':
	import boilerplate, time, resource
	t = time.time()
	r = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
	#boilerplate.all(main(500), t, r)
	boilerplate.all(main(500), t, r)