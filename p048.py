'''

The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.

Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.

'''

def main():
	n = 1000
	series = [i**i for i in xrange(1,n+1)]
	ret = str(sum(series)) #sum the lsit and then stringify ans so we can trim it
	return ret[-10:] #last 10 digits

if __name__ == '__main__':
	import boilerplate, time, resource
	t = time.time()
	r = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
	boilerplate.all(main(), t, r)
