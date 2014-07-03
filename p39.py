def main(): # maximize number of solutions for the equation:
	# p = a + b + c, where p is the perimeter of a right triangle and a, b, c, and integer side lengths

	max_num_solutions = 0
	best_p = 0

	# O(n^3) ... but still under a second with pypy
	for p in range(3,1000):
		num_solutions = 0
		for a in xrange(1,p/2):
			for b in xrange(a,p/2): # 'a' because of symmetry
				c = p - a - b
				if (c**2 == a**2 + b**2):
					if (a > 0 and b > 0 and c > 0):
						num_solutions += 1

		if num_solutions > max_num_solutions:
			#print num_solutions, p #uncomment if you want to see it in action
			max_num_solutions = num_solutions
			best_p = p 

	return best_p

if __name__ == '__main__':
	import boilerplate, time
	boilerplate.all(time.time(),main())
