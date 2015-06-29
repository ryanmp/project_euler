def main(n): # Longest Collatz sequence from a starting # less than 1,000,000 = n
	for i in xrange(1,n):
		longest_chain = 1
		this_chain_length = 1
		while (i != 1):
			this_chain_length += 1
			i = run_rule_on(i)
		longest_chain = max(this_chain_length, longest_chain)
	return longest_chain

def run_rule_on(n):
	if (n%2==0): return n/2 # even
	else: return (3*n) + 1 # odd

if __name__ == '__main__':
	import boilerplate, time
	boilerplate.all(time.time(),main(1000000))
