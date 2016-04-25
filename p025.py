def main(): # which term in fib-seq is the first with 1000 digits
	n = 1000

	a = 1
	b = 1
	count = 3
	while (len(str(a+b))) < n:
		temp = b
		b = a + b
		a = temp
		count += 1
	return count
	
if __name__ == '__main__':
	import boilerplate, time, resource
	t = time.time()
	r = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
	boilerplate.all(main(), t, r)
