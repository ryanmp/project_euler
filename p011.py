import numpy
def main(): # greatest product of 4 adjacent numbers (8 diff directions including diagonal)
	lines = open('p011.in').read().split('\n') #file -> list
	arr = []
	for i in lines:
		temp = i.split(' ')
		arr.append( [int(x) for x in temp] )

	biggest_prod = 0
	for i in xrange(16): # might need to go to 20 with one of these... 
		for j in xrange(16): #(i,j) is starting idx

			combos = []
			combos.append( [arr[i+x][j] for x in xrange(4)] )#down
			combos.append( [arr[i][j+x] for x in xrange(4)] )#right

			if i < 16:
				combos.append( [arr[i+x][j+x] for x in xrange(4)] )#diag_DR

			if i > 4:
				combos.append( [arr[i-x][j+x] for x in xrange(4)] )#diag_DL

			for n in combos:
				prod = numpy.product(n)
				biggest_prod = max(prod, biggest_prod)

	return 'biggest_prod', biggest_prod

if __name__ == '__main__':
	import boilerplate, time
	boilerplate.all(time.time(),main())
