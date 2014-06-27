import numpy
def main(n): #Find the thirteen adjacent digits in the 1000-digit number that have the greatest product. What is the value of this product?
	f = list(open('p8.in').read().replace(" ", "")) #file -> list
	f = [int(x) for x in f] #chars -> ints
	biggest_prod = 0
	for i in xrange(len(f)-n):
		prod = numpy.product(f[i:i+n])
		biggest_prod = max(prod, biggest_prod)
	return biggest_prod

if __name__ == '__main__':
	import boilerplate, time
	boilerplate.all(time.time(),main(13))
