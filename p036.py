'''
The decimal number, 585 = 1001001001 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2

'''

def is_palindrome(n):
	return str(n) == str(n)[::-1]

def main(): 
	sum = 0
	for i in xrange(1,int(1e6)):
		if is_palindrome(i):
			if (is_palindrome(bin(i)[2:])):
				sum += i
				print i, bin(i)[2:]

	return sum

if __name__ == '__main__':
	import boilerplate, time
	boilerplate.all(time.time(),main())
