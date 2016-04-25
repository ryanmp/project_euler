'''

A perfect number is a number for which the sum of its proper divisors is exactly equal to the number.
For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16,
the smallest number that can be written as the sum of two abundant numbers is 24.
By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers.
However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot
be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.

'''

def main():
	num = 28123
	x = get_all_abundant(num)
	y = get_all_abundant_sums(x)
	z = get_target_numbers(num,y) # all_numbers - abundant_sums
	return sum(z)

# return all divisors other than n itself
def proper_divisors(n):
	ret = []
	for i in xrange(1,int(n/2)+1):
		if n%i == 0:
			ret.append(i)
	return ret

# info: is the sum of the proper divisors of n larger than n?
# input: single value for n to be checked
def is_abundant(n):
	return sum(proper_divisors(n)) > n

# info: runs is_abundant on each value in range 1-n
def get_all_abundant(n):
	l = []
	for i in xrange(n):
		#print i
		if is_abundant(i)==1:
			l.append(i)
	return l

# input: array of abundant numbers
# returns: an array of sums made from a+b abundant numbers
def get_all_abundant_sums(arr):
	sums = set()
	for i in xrange(0,len(arr)):
		for j in xrange(i,len(arr)):
			sums.add(arr[i]+arr[j])
	return sums

# input: n, all_abundant_sums as set
# returns: a set of the numbers which fulfill the problem requirements
def get_target_numbers(n,arr_set):
	l = set([i for i in xrange(1,n)])
	return l-arr_set

if __name__ == '__main__':
	import boilerplate, time, resource
	t = time.time()
	r = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
	boilerplate.all(main(), t, r)





	