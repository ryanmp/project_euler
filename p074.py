
'''
digit factorial chains
e.g.: 145 -> 1! + 4! + 5! = 145 (this one repeats every iteration)
How many chains, with a starting number below one million,
contain exactly sixty non-repeating terms?
'''
from math import factorial
def main(n):
	how_many_chains = 0 # contain exactly 60 non-repeating terms?
	for i in xrange(1,int(n)):
		if chain_length(i) == 60:
			how_many_chains += 1
	return how_many_chains

def dig_fac_sum(n):
	ret_sum = 0
	arr = [int(i) for i in list(str(n))]
	for i in arr:
		ret_sum += factorial(i)
	return ret_sum

def chain_length(n):
	ret_length = 0
	terms = set([])
	while n not in terms:
		terms.add(n)
		ret_length += 1
		n = dig_fac_sum(n)
	return ret_length

if __name__ == '__main__':
	import boilerplate, time
	# method seems accurate, but it's about 100x too slow...
	# todo: look for ways to improve algo speed
	boilerplate.all(time.time(),main(1e4)) # shooting for 1e6 in 1 second