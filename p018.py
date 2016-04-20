def main(): # maximum path-sum from top to bottom

	# input to array ( 'p18_test.in' for a smaller test set )
	lines = open('p018.in').read().split('\n') #file -> list
	arr = []
	for i in lines:
		temp = i.split(' ')
		arr.append( [int(x) for x in temp] )

	# recursively sum through all possible paths, keeping the largest sum
	def add_next(my_sum,arr,row,idx,biggest_sum):
		my_sum += arr[row][idx]
		row += 1
		if row<len(arr):
			if (idx - 1 >= 0):
				biggest_sum = add_next(my_sum,arr,row,idx-1,biggest_sum) # idx-1
			if (idx + 1 <= len(arr[row])):
				biggest_sum = add_next(my_sum,arr,row,idx+1,biggest_sum) # idx+1
			biggest_sum = add_next(my_sum,arr,row,idx,biggest_sum) # same idx

		biggest_sum = max(my_sum, biggest_sum)
		return biggest_sum

	return add_next(0,arr,0,0,0)

if __name__ == '__main__':
	import boilerplate, time, resource
	t = time.time()
	r = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
	boilerplate.all(main(), t, r)
