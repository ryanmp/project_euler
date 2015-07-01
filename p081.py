'''
Find the minimal path sum, in a 80 by 80 matrix,
from the top left to the bottom right by only moving right and down.

for my test version, the solution should be 2427

i get the general idea... (continued sums of min route along the diags)
but keeping track of diagonals of a 2d array using x,y indexing is
really difficult to keep track of. 

I'm going to move on to an earlier problem for now...


'''
from random import random
import pprint


def custom_mod(x,divider):
	if x < divider:
		return 0
	else:
		return x%divider

lines = open('p081_test.in').read().split('\n')
arr = []
for i in lines:
	temp = i.split(',')
	arr.append( [int(x) for x in temp] )

pprint.pprint(arr)	

prev_diag = []
next_diag = []
best_so_far = []
end_idx = 0
inc = 0
for i in xrange(len(arr)+len(arr[0]) - 1):
	print 'diag: ' + str(i) + '------------------'
	start_idx = min(len(arr)-1,i)
	first_idx = start_idx
	
	if (i > len(arr)-1):
		inc += 1
		end_idx = inc
	else:
		end_idx = 0
	
	#print 'calc rel', str(i), str(end_idx), custom_mod(i, len(arr))

	prev_diag = best_so_far
	next_diag = []
	while (end_idx <= first_idx):
		print start_idx, end_idx
		next_diag.append(arr[start_idx][end_idx])
		start_idx -= 1
		end_idx += 1
	
	best_so_far = []
	for j in xrange(0,len(next_diag)):
		this_sum = next_diag[j]
		opt1 = 10000
		opt2 = 10000
		amount_to_add = 0
		if (len(prev_diag) > 0 and j < len(prev_diag)):
			opt1 = prev_diag[j]
		if (len(prev_diag) > 0 and j >= 1):
			opt2 = prev_diag[j-1]
		amount_to_add = min(opt1,opt2)
		if (i > 0):
			this_sum += amount_to_add
		best_so_far.append(this_sum)

	print 'p:' + str(prev_diag)
	print 'n:' + str(next_diag)
	print 'b:' + str(best_so_far)








def main():
	lines = open('p081_test.in').read().split('\n')
	arr = []
	for i in lines:
		temp = i.split(',')
		arr.append( [int(x) for x in temp] )

	 # finds the solution in the 5x5 matrix in less than 1000 rand runs
	return run_random_trip(arr,1000)
	

def run_random_trip(arr,num_trials):
	min_path_sum = 999999
	for i in xrange(num_trials):
		new_path_sum = random_trip(arr)
		if new_path_sum < min_path_sum:
			min_path_sum = new_path_sum
			print new_path_sum

	return min_path_sum




def random_trip(arr):
	x = 0
	y = 0
	path_sum = 0
	num_steps_in_path = len(arr[0]) + len(arr) - 1
	for i in xrange(num_steps_in_path): 
		path_sum += arr[x][y]
		if x == len(arr[0])-1: y += 1
		elif y == len(arr)-1: x += 1
		else:
			if random() > .5: x += 1
			else: y += 1
	return path_sum

'''
if __name__ == '__main__':
	import boilerplate, time
	boilerplate.all(time.time(),main())
'''


