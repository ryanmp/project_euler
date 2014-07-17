'''
Considering natural numbers of the form, ab, where a, b < 100,
what is the maximum digital sum?
'''

def main(n):
	maximum_digit_sum = 0
	for a in xrange(n):
		for b in xrange(n):
			new_sum = digit_sum(a**b)
			maximum_digit_sum = max(new_sum, maximum_digit_sum)
	return maximum_digit_sum

# in: an integer n
# out: the sum of the digits in n
def digit_sum(n):
	return sum([int(i) for i in list(str(n))])

if __name__ == '__main__':
	import boilerplate, time
	# brute force works just fine... ( t < 1 second)
	#  assuming that python is able to store all the digits for these
	#  very long ints. This assumption needs testing.
	boilerplate.all(time.time(),main(100))
