def main():
	x = set([i for i in range(0,1000,3)])
	y = set([i for i in range(0,1000,5)])
	return sum(x | y)

if __name__ == '__main__':
	import boilerplate, time
	boilerplate.all(time.time(),main())