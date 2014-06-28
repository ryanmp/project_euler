def main(n): # sum of the digits of the number 2^1000 ?
	x = list(str(2**n)) # calc -> str -> array of chars
	return sum([int(i) for i in x]) # chars -> ints -> sum it!

if __name__ == '__main__':
	import boilerplate, time
	boilerplate.all(time.time(),main(1000))