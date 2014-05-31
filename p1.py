import boilerplate
def main():
	x = set([i for i in range(0,1000,3)])
	y = set([i for i in range(0,1000,5)])
	return sum(x | y)

if __name__ == '__main__':
	boilerplate.all(main())