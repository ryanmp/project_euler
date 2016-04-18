from functools import reduce 
import operator

def main(n): #Find the thirteen adjacent digits in the 1000-digit number that have the greatest product. What is the value of this product?
	f = list(open('p008.in').read().replace(" ", "")) #file -> list
	f = [int(x) for x in f] #chars -> ints

	biggest_prod = 0
	for i in xrange(len(f)-n):
		prod = reduce(operator.mul, f[i:i+n], 1)
		biggest_prod = max(prod, biggest_prod)
	return biggest_prod

if __name__ == '__main__':
	import boilerplate, time, resource
	t = time.time()
	r = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
	boilerplate.all(main(13), t, r)
