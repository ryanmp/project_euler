from itertools import combinations
def main(_n): # how many value for nCr, 1 < n < 100, exceed 1 mil?

	# ahh yes, the dreaded O(n!)... 'combinations' is quite the bottleneck
	count = 0
	for n in xrange(1,_n):
		for r in xrange(1,n+1): # if r > n... nCr = 0
			#l = len(list(combinations([i for i in xrange(n)],r))) #n choose r
			
			# a little faster than previous line
			i = combinations([i for i in xrange(n)],r)
			l = sum(1 for e in i)

			if l > 1000000: count += 1

	return count

if __name__ == '__main__':
	import boilerplate, time
	boilerplate.all(time.time(),main(24)) # good luck getting this all the way to 100
	print 'not finished yet... shooting for n=100'