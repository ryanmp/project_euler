import math

def pentagonal_number(n):
	return n*(3*n-1)/2

def is_pentagonal(n):
	x = (1 + math.sqrt(24*n + 1))/6
	return x == int(x)

def main():
	a = 0
	while (True):
		for b in xrange(a-1, 0, -1):

			j, k = pentagonal_number(b), pentagonal_number(a)
			jk_sum, kj_diff = j + k, k - j
			
			if is_pentagonal(jk_sum) and is_pentagonal(kj_diff):
				return kj_diff
				
		a += 1

if __name__ == '__main__':
	import boilerplate, time, resource
	t = time.time()
	r = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
	boilerplate.all(main(), t, r)
