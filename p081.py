'''
Find the minimal path sum, in a 80 by 80 matrix,
from the top left to the bottom right by only moving right and down.
'''


def main(file_name):

	lines = open(file_name).read().split('\n')
	arr = []
	for i in lines:
		temp = i.split(',')
		arr.append( [int(x) for x in temp] )

	for i in xrange(len(arr)):
	    for j in xrange(len(arr[0])):

	    	if i*j > 0:
	    		arr[i][j] += min(arr[i-1][j], arr[i][j-1])
	    	elif i:
    			arr[i][j] += arr[i-1][j]
    		elif j:
    			arr[i][j] += arr[i][j-1]

	 
	return arr[-1][-1]



if __name__ == '__main__':
	import boilerplate, time
	boilerplate.all(time.time(),main('p081.in'))



