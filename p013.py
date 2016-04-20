'''

Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.
(in included file)

'''

def main(): 
	arr = [int(x) for x in open('p013.in').read().split('\n')] #file -> num_list
	ret = str(sum(arr)) #sum num_list and then stringify ans so we can trim it
	return int(ret[0:10]) #first 10 digits

if __name__ == '__main__':
	import boilerplate, time, resource
	t = time.time()
	r = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
	boilerplate.all(main(), t, r)
