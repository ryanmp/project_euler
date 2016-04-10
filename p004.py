'''

A palindromic number reads the same both ways.
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.

Find the largest palindrome made from the product of two 3-digit numbers.

'''

def main():
	biggest = 0
	for i in xrange(999, 100, -1):
		for j in xrange(999, i, -1):
			x = i*j
			if x > biggest and is_palindrome(x): #checking x > biggest first since it is a cheaper operation
				biggest = x

	return biggest

def is_palindrome(n):
	return str(n) == str(n)[::-1]

if __name__ == '__main__':
	import boilerplate, time, resource
	t = time.time()
	r = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
	boilerplate.all(main(), t, r)

