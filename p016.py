'''

2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?

'''

import math
def main(): 
	n = 1000
	x = list(str(2**n)) # calc -> str -> array of chars
	return sum([int(i) for i in x]) # chars -> ints -> sum it!

if __name__ == '__main__':
	import boilerplate, time, resource
	t = time.time()
	r = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
	boilerplate.all(main(), t, r)
