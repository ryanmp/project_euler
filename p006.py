'''

The sum of the squares of the first ten natural numbers is,

1^2 + 2^2 + ... + 10^2 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)^2 = 55^2 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers
and the square of the sum is 3025 - 385 = 2640.

Find the difference between the sum of the squares
of the first one hundred natural numbers and the square of the sum.

'''

def main():
	n = 100
	square_of_sums = sum([i for i in xrange(1,n)])
	square_of_sums *= square_of_sums
	sum_of_squares = sum([i*i for i in xrange(1,n)])
	return square_of_sums - sum_of_squares

if __name__ == '__main__':
	import boilerplate, time, resource
	t = time.time()
	r = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
	boilerplate.all(main(), t, r)
