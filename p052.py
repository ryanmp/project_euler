'''

It can be seen that the number, 125874, and its double, 251748,
contain exactly the same digits, but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.

'''


def contains_same_digits(x,y):
	return set(str(x)) == set(str(y))

def main():
	for x in xrange(1,1000000):
		m = [3,4,5,6]
		ls = [m*x for m in [3,4,5,6]]
		matches = 0
		for l in ls:
			if not contains_same_digits(x*2,l):
				break
			else:
				matches += 1
		if matches == 4:
			return x	

if __name__ == '__main__':
	import boilerplate, time
	boilerplate.all(time.time(),main()) 
