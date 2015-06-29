def main(): # first 10 digits of the sum of the following 100, 50-digit numbers
	arr = [int(x) for x in open('p013.in').read().split('\n')] #file -> num_list
	ret = str(sum(arr)) #sum num_list and then stringify ans so we can trim it
	return int(ret[0:10]) #first 10 digits

if __name__ == '__main__':
	import boilerplate, time
	boilerplate.all(time.time(),main())
