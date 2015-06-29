from itertools import permutations
from math import factorial as f
'''
Q: What is the millionth lexicographic permutation
of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
'''
def main():
	p = permutations([0,1,2,3,4,5,6,7,8,9])
	# lists them in lexicographic order by default
	l = list(p)
	ans = l[1000000-1] #Why the '-1'? l[0] is the first permutation
	return join_ints(ans)

# input: array of ints
# e.g.: [1,2,3,4]
# output: a single int
# e.g.: 1234
def join_ints(l):
	l = [str(i) for i in l] # to array of chars
	as_str = ''.join(l)
	return int(as_str)

if __name__ == '__main__':
	import boilerplate, time
	boilerplate.all(time.time(),main())
	# ha! So originally I started with the math
	# approach, thinking that the factorials would
	# slow us down - but then I went back and tested
	# the naive approach and it still takes less than
	# 5 seconds... so that's what I have down here,
	# for simplicity sake