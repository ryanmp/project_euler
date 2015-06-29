def main(n):
	series = [i**i for i in xrange(1,n+1)]
	ret = str(sum(series)) #sum the lsit and then stringify ans so we can trim it
	return ret[-10:] #last 10 digits

if __name__ == '__main__':
	import boilerplate, time
	boilerplate.all(time.time(),main(1000))
