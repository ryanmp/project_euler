# Find the sum of 'all' the positive integers (less than 28123) which
# cannot be written as the sum of two abundant numbers.
def main(num):
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
	s = sum(proper_divisors(n))
	if s==n: return -1
	elif s>n: return 1
	else: return 0

# info: runs is_abundant on each value in range 1-n
def get_all_abundant(n):
	l = []
	for i in xrange(n):
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
	import boilerplate, time
	boilerplate.all(time.time(),main(28123))   # goal: 28123
	# current time: under 5 seconds with pypy