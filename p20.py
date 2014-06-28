import math
def main(n): # Find the sum of the digits in the number 100! (100 factorial)
	x = list(str(math.factorial(n))) # calc -> str -> array of chars
	return sum([int(i) for i in x]) # chars -> ints -> sum it!

if __name__ == '__main__':
	import boilerplate, time
	boilerplate.all(time.time(),main(100))