# find the value of: (where d stands for a particular digit)
# d_1 x d_10 x d_100 x d_1000 x d_10000 x d_100000 x d_1000000
# for this crazy number: 012345678910111213...
def main(): 

	# represent Champernowne's constant as one nice long string
	n = [str(i) for i in xrange(0,1000001)] 
	a = "".join(n)

	# these are the digits we want to multiply 1, 10, 100, etc..
	idxs = [10**i for i in xrange(7)]

	product = 1 # always start a product at 1 (rather than zero for a sum)
	for idx in idxs:
		product *= int(a[idx])
	return product

if __name__ == '__main__':
	import boilerplate, time
	boilerplate.all(time.time(),main())



