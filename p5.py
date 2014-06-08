def main(): #brute force is too slow...
	#I'll replace it with a better method later 
	n = 2*3*5*7*11*13*17*19
	while(True):
		is_solution = True
		for i in range(2,20):
			if n%i != 0:
				is_solution = False
				break
		if (is_solution):
			return n
		n += 1

if __name__ == '__main__':
	import boilerplate
	boilerplate.all(main())
