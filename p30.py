import math
def main(): # sum of all the numbers, s.t. n = n[0]^5 + n[1]^5 ...
	# I assume we will be restricting this to 5 digit numbers,
	# else... what about zeroes??? e.g. 12305 is equiv to 123005 for this problem 
	all_passing_numbers = []
	for i in xrange(10000, 99999):
		if is_a_digit_fifth_power(i):
			all_passing_numbers.append(i)

	return sum(all_passing_numbers)

def is_a_digit_fifth_power(n):
	arr = [int(i)**5 for i in str(n)]
	return (n == sum(arr))

if __name__ == '__main__':
	import boilerplate, time
	boilerplate.all(time.time(),main())
