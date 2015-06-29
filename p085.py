from math import fabs

def main():
	'''
	I know our target rectangle will be between 1x1 and 2000x2000...
	but it will take too long to check this entire range,
	So I'm assuming a smaller range of values to look through

	note to future self:
	--------------------
	what about determing this range dynamically? i.e., start at 1x1, 1x2...
	until we exceed target...
	then return to 2x2, 2,3... and so on
	would that be quick enough?

	and to take it even one step further...
	binary search for closest solution for a given x in (x,n)
	for x=1: 1x1000 -> 1x1500 -> 1x1750 -> 1x1875

	'''
	search_range = 60
	target = 2000000
	min_diff = target
	min_diff_d = (0,0)
	#also hardcoded search_range in here (46)

	for i in xrange(search_range,46,-1): 
		for j in xrange(search_range,i,-1):
			n = count_rectangles((i,j))
			if fabs(n-target) < min_diff:
				min_diff = fabs(n-target)
				min_diff_d = (i,j)
				print min_diff, min_diff_d


	'''
	for i in xrange(1,2000): 
		n = count_rectangles((i,1))
		if fabs(n-target) < min_diff:
			min_diff = fabs(n-target)
			min_diff_d = (i,1)
			print min_diff, min_diff_d
	'''

	return min_diff_d[0]*min_diff_d[1]

def how_many_fit(s,l): #small, large
	assert(s[0] <= l[0] and s[1] <= l[1])
	ret = 0
	for i in xrange(l[0]-s[0]+1):
		for j in xrange(l[1]-s[1]+1):
			ret += 1
	return ret

def count_rectangles(l):
	total = 0
	for i in xrange(1,l[0]+1):
		for j in xrange(1,l[1]+1):
			ans = how_many_fit((i,j),l)
			total += ans
	return total

if __name__ == '__main__':
	import boilerplate, time
	boilerplate.all(time.time(),main())
