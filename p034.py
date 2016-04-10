import math
def main(n): # sum of all digital factorial numbers.... 
	# How can I come up with a bound for this?

	all_passing_numbers = []
	for i in xrange(3, n):
		if is_a_digit_factorial(i):
			all_passing_numbers.append(i)

	'''
	factorials = []
	for i in xrange(1,20):
		factorials.append(math.factorial(i))
	print factorials
	'''

	# not a complete solutions... just returns the sum of a couple of them
	return sum(all_passing_numbers)

def is_a_digit_factorial(n):
	arr = [math.factorial(int(i)) for i in str(n)]
	return (n == sum(arr))

if __name__ == '__main__':
	import boilerplate, time, resource
	t = time.time()
	r = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
	boilerplate.all(main(90000), t, r)
