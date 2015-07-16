'''

Find the number of integers 1 < n < 10^7, for which n
and n + 1 have the same number of positive divisors.
For example, 14 has the positive divisors 1, 2, 7, 14 while 15 has 1, 3, 5, 15.

solution:


'''

from math import sqrt, ceil, floor

def num_divisors(n):
	count = 0
	# something like this should work, right?
	# although, even w/ this speed up, still 1e2 too slow
	for i in xrange(1,int(sqrt(n))): 
	#for i in xrange(1,n+1):
		if n%i==0:
			count += 1
	return count*2

def is_solution(n):
	if num_divisors(n) == num_divisors(n+1):
		return True
	else:
		return False

def main():
	num_solutions = 0
	for i in xrange(2,int(1e5)):
		if is_solution(i):
			num_solutions += 1
	return num_solutions

if __name__ == '__main__':
	import boilerplate, time
	boilerplate.all(time.time(),main())