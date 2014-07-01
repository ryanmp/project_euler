def main(): # maximum path-sum from top to bottom
	lines = open('p18.in').read().split('\n') #file -> list
	arr = []
	for i in lines:
		temp = i.split(' ')
		arr.append( [int(x) for x in temp] )

	sum = 0
	for line in arr:
		sum += line[0]

	return 'not finished yet!'

if __name__ == '__main__':
	import boilerplate, time
	boilerplate.all(time.time(),main())
