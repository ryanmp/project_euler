def main():
	n = 100
	square_of_sums = sum([i for i in xrange(1,n)])
	square_of_sums *= square_of_sums
	sum_of_squares = sum([i*i for i in xrange(1,n)])
	return square_of_sums - sum_of_squares

if __name__ == '__main__':
	import boilerplate
	boilerplate.all(main())
