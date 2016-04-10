'''

The decimal number, 585 = 1001001001 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2

'''

def is_palindrome(n):
	return str(n) == str(n)[::-1]

def main(): 
	sum = 0
	for i in xrange(1,int(1e6),2): # via logic, no even solutions - 01...10 (can't start with a zero)
		if is_palindrome(i):
			if (is_palindrome(bin(i)[2:])):
				sum += i
	return sum

if __name__ == '__main__':
	import boilerplate, time, resource
	t = time.time()
	r = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
	boilerplate.all(main(), t, r)
