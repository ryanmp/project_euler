'''
Starting from zero the natural numbers are written down
in base 10 like this: 
0 1 2 3 4 5 6 7 8 9 10 11 12....

Consider the digit d=1. After we write down each number n,
we will update the number of ones that have occurred and
call this number f(n,1).

...and then there are several more steps. This appears to be
yet another problem in which the upper bound for the search
isn't obvious to me.

'''

def main():

	n = 12
	d = 1

	ints = [i for i in xrange(0,n+1)]
	digit_counts = []
	for i in ints:
		counts = []
		for dig in xrange(10):
			temp = str(i)
			counts.append(temp.count(str(dig)))
		digit_counts.append(counts)

	#effectively sums the columns
	digit_sums = [ sum(x) for x in zip(*digit_counts[:n+1]) ] 

	print digit_sums[d] # f(n,d)
	return 'not finished'

if __name__ == '__main__':
	import boilerplate, time
	boilerplate.all(time.time(),main())