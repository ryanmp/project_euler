'''
We shall define an 'almost equilateral' triangle to be a
triangle for which two sides are equal and the third differs
by no more than one unit.

Find the sum of the perimeters of all 'almost equilateral'
triangles with integral side lengths and area and whose perimeters
do not exceed one billion (1,000,000,000).

note:
first off I'm using a dumb brute-force way which calculates all the
possibilities and sums the perimeters of the ones fitting the constraints
...and as always, there must be a better way - right?

'''

from math import sqrt, fabs

def main():
	sum_perimeters = 0

	for i in xrange(2,200000): #333333334
		a = area(i,i,i-1)
		if is_int(a):
			sum_perimeters += (i+i+i-1)
			print i,i,i-1, a
		a = area(i,i,i+1)
		if is_int(a):
			sum_perimeters += (i+i+i+1)
			print i,i,i+1, a

	print sum_perimeters
	return 'not-done'

def area(a,b,c):
	s = (a+b+c)/2.0
	ans = sqrt(s*(s-a)*(s-b)*(s-c))
	return ans

def is_int(x):
	if fabs(x - int(x)) < .000000001: return True
	else: return False

if __name__ == '__main__':
	import boilerplate, time
	boilerplate.all(time.time(),main())
	

