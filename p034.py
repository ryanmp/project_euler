'''

145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.

'''

import math

f = {}
for i in xrange(0,10):
	f[i] = math.factorial(i)

def main(): 

	# hm... still pretty slow... there's gotta be some tricks to speed this one up
	n = 2540160 # since 9!*7 = 2540160

	all_passing_numbers = []
	for i in xrange(3, n):
		if is_a_digit_factorial(i):
			all_passing_numbers.append(i)

	return sum(all_passing_numbers)

'''
def is_a_digit_factorial(n):
	arr = [math.factorial(int(i)) for i in str(n)]
	return (n == sum(arr))
'''

def is_a_digit_factorial(n):
	arr = [int(i) for i in str(n)]
	arr.sort(reverse=True)
	result = 0
	for i in arr:
		result += f[i]
		if result > n:
			return False
	return n == result

if __name__ == '__main__':
	import boilerplate, time, resource
	t = time.time()
	r = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
	boilerplate.all(main(), t, r)
