'''

If we take 47, reverse and add, 47 + 74 = 121, which is palindromic.

Not all numbers produce palindromes so quickly. For example,

349 + 943 = 1292,
1292 + 2921 = 4213
4213 + 3124 = 7337

That is, 349 took three iterations to arrive at a palindrome.

Although no one has proved it yet, it is thought that some numbers, like 196, never produce a palindrome. A number that never forms a palindrome through the reverse and add process is called a Lychrel number. Due to the theoretical nature of these numbers, and for the purpose of this problem, we shall assume that a number is Lychrel until proven otherwise. In addition you are given that for every number below ten-thousand, it will either (i) become a palindrome in less than fifty iterations, or, (ii) no one, with all the computing power that exists, has managed so far to map it to a palindrome. In fact, 10677 is the first number to be shown to require over fifty iterations before producing a palindrome: 4668731596684224866951378664 (53 iterations, 28-digits).

Surprisingly, there are palindromic numbers that are themselves Lychrel numbers; the first example is 4994.

How many Lychrel numbers are there below ten-thousand?

NOTE: Wording was modified slightly on 24 April 2007 to emphasise the theoretical nature of Lychrel numbers.

'''

def main():
	n = 10000
	how_many_lych_nums = 0
	for i in xrange(1,n+1):
		if is_lych_num(i):
			how_many_lych_nums += 1
	return how_many_lych_nums

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
	import boilerplate, time, resource
	t = time.time()
	r = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
	boilerplate.all(main(), t, r)

