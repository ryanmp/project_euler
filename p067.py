def main(): # same as p18... but with a much larger test set

	lines = open('p067.in').read().split('\n') #file -> list
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
	import boilerplate, time
	boilerplate.all(time.time(),main()) # about 1 second... not too bad
