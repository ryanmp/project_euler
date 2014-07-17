'''
Lychrel numbers:
How many Lychrel numbers are there below ten-thousand?
(A big caveat -  we are assuming that if it doesn't become a palindrome within 50
	iterations, then it is a Lychrel number)

'''

def main(n):
	how_many_lych_nums = 0
	for i in xrange(1,n+1):
		if is_lych_num(i):
			how_many_lych_nums += 1
	return how_many_lych_nums

# input: array of ints
# e.g.: [1,2,3,4]
# output: a single int
# e.g.: 1234
def join_ints(l):
	l = [str(i) for i in l] # to array of chars
	as_str = ''.join(l)
	return int(as_str)

# e.g.s 
# in: 123, out: false
# in: 121, out: true
def is_palindrome_num(n):
	return str(n) == str(n)[::-1]

# e.g. in: 123, out: 321
def reverse_int(n):
	s = str(n)
	s = s[::-1]
	return int(s)

# true IF recursively adding the reverse int to itself
# eventually leads to a palindrome number
def is_lych_num(n):
	max_iterations = 50
	idx = 0

	def inner(n,idx):
		n = n + reverse_int(n) 
		if is_palindrome_num(n):
			return False
		else:
			if idx>=max_iterations:
				return True
			else:
				idx += 1
				return inner(n,idx)

	return inner(n, idx)

if __name__ == '__main__':
	import boilerplate, time
	boilerplate.all(time.time(),main(10000))


