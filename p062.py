'''
Find the smallest cube for which exactly five permutations
of its digits are also cubes.



'''
import math
from itertools import permutations
def main(n):

	
	base = 6407 # should get to n == 3 within a couple iterations
	while(True):
		count_p = 0
		base += 1
		cube = base**3
		p = get_permutations(cube)
		for i in p:
			if is_cube(i):
				print i,'is cube...'
				count_p += 1
			if count_p >= n:
				return cube
		print count_p
	return 0

def is_cube(n):
	x = math.pow(n,1.0/3) #cubic root
	x = int(round(x))
	if x**3 == n:
		return True
	else:
		return False


# note: this functions uses join_ints()
def get_permutations(_n):
	n = [int(i) for i in list(str(_n))] # int -> list of ints


	# dev-note:
	# I probably shouldn't be listing permutations.. instead I should use it like a generator,
	# and just check each value individually...


	ret = [join_ints(i) for i in list(permutations(n))]
	'''
	this solves my original interpretation of this problem, but 10**3
	 seems like too easy of a candidate, since the number 1000
	 technically has 6 permutations which are all the same, and all cubes
	so converting to a set guarantees only unique permutations...
	 but what about numbers like 000125? should this be interpreted as 125,
	 or should it be disallowed?
	if I wanted to not include the variations with leading zeroes, I could
	 check for length... and only return list_ints with the same length as
	 the input...
	'''
	#return ret
	#return set(ret)
	# just ones of the same number of digits at n
	ret = set(ret)
	l = len(str(_n))
	ret = [i for i in ret if len(str(i)) == l]
	return ret

def join_ints(l):
	l = [str(i) for i in l] # to array of chars
	as_str = ''.join(l)
	return int(as_str)


if __name__ == '__main__':
	import boilerplate, time
	boilerplate.all(time.time(),main(3))

