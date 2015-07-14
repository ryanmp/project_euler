'''

Some positive integers n have the property that the sum
[ n + reverse(n) ] consists entirely of odd (decimal) digits.
For instance, 36 + 63 = 99 and 409 + 904 = 1313. We will call
such numbers reversible; so 36, 63, 409, and 904 are reversible.
Leading zeroes are not allowed in either n or reverse(n).

There are 120 reversible numbers below one-thousand.

How many reversible numbers are there below one-billion (10^9)?

solution:
I've got a basic solution which works for small n (10^5)

'''

def reverse_n(n):
	l = list(str(n))
	l.reverse()
	return int(''.join(l))

def all_odd_digits(n):
	l = [int(i) for i in list(str(n))]
	for digit in l:
		if (digit%2 != 1):
			return False
	return True

def is_reversible(n):
	n2 = reverse_n(n)
	if len(str(n)) != len(str(n2)): # removing entries w/ leading zeroes
		return False 
	ret = all_odd_digits(n + n2)
	#if (ret):
	#	print n, n2, (n+n2), ret
	return all_odd_digits(n + reverse_n(n))

def main():
	n_reversible_numbers = 0
	max_n = 200000
	for i in xrange(1,max_n+1):
		if is_reversible(i):
			n_reversible_numbers += 1

	return n_reversible_numbers

if __name__ == '__main__':
	import boilerplate, time
	boilerplate.all(time.time(),main())