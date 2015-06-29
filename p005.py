# What is the smallest positive number that is
# evenly divisible by all of the numbers from 1 to 20?
# 1-10: 2520
def main(n):

	smallest = n
	while(True):
		passes = True
		for i in xrange(2,n+1):
		#for i in xrange(11,n+1): # don't need to do all 1-20
			if smallest%i != 0:
				passes = False
				break

		if (passes):
			return smallest
		else:
			smallest += 1

if __name__ == '__main__':
	import boilerplate, time
	boilerplate.all(time.time(),main(20)) # 5 seconds, calling it good
