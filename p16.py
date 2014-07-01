import math
def main(n): # Find the sum of the digits in the number 2**1000
	x = list(str(2**n))) # calc -> str -> array of chars
	return sum([int(i) for i in x]) # chars -> ints -> sum it!

if __name__ == '__main__':
	import boilerplate, time
	boilerplate.all(time.time(),main(1000))