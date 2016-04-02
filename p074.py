
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


f = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]

def dig_fac_sum(n):
	tmp = n
	result = 0
	while tmp > 0:
		result += f[tmp%10]
		tmp = tmp/10
	return result


d = {}

def chain_length(n):
	ret_length = 0
	terms = set([])
	start_n = n

	while n not in terms:
		if n in d:
			ret_length += d[n]
			break
		else:
			terms.add(n)
			ret_length += 1
			n = dig_fac_sum(n)

	d[start_n] = ret_length

	return ret_length

if __name__ == '__main__':
	import boilerplate, time

	boilerplate.all(time.time(),main(1e6)) # 2 seconds with caching... not great but it'll have to do for now