'''

The following iterative sequence is defined for the set of positive integers:

n -> n/2 (n is even)
n -> 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms.
Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.

'''

d = {}

def main(): # Longest Collatz sequence from a starting # less than 1,000,000 = n
	n = 1000000
	for i in xrange(1,n):
		longest_chain = 1
		this_chain_length = get_chain_len(i)
		#this_chain_length = get_chain_len_no_dict(i)

		if i not in d:
			d[i] = this_chain_length
			
		longest_chain = max(this_chain_length, longest_chain)
	return longest_chain

def run_rule_on(n):
	if (n%2==0): return n/2 # even
	else: return (3*n) + 1 # odd

def get_chain_len(n, printing = None):
	this_chain_length = 1
	while (n != 1):
		if (printing):
			print '.', n
		n = run_rule_on(n)
		if n in d:
			return d[n] + this_chain_length
		this_chain_length += 1
	return this_chain_length

def get_chain_len_no_dict(n, printing = None): #about 10x faster
	this_chain_length = 1
	while (n != 1):
		if (printing):
			print '.', n
		this_chain_length += 1
		n = run_rule_on(n)
	return this_chain_length

if __name__ == '__main__':
	import boilerplate, time, resource
	t = time.time()
	r = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
	boilerplate.all(main(), t, r)

