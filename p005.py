'''

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?


'''

def main():

	divisors = [11, 13, 14, 16, 17, 18, 19, 20]

	smallest = 2520
	while(True):
		passes = True
		for i in divisors:
			if smallest%i != 0:
				passes = False
				break

		if (passes):
			return smallest
		else:
			smallest += 2520

if __name__ == '__main__':
	import boilerplate, time, resource
	t = time.time()
	r = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
	boilerplate.all(main(), t, r)
