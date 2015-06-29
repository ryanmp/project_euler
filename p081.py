'''
Find the minimal path sum, in a 80 by 80 matrix,
from the top left to the bottom right by only moving right and down.

I think this can be done via dynamic programming,
I'm just a little rusty+newbie at the technique,
so it will require some thought

'''
from random import random


def main():
	lines = open('p081.in').read().split('\n')
	arr = []
	for i in lines:
		temp = i.split(',')
		arr.append( [int(x) for x in temp] )

	print run_random_trip(arr,1000)
	return 'not-done'
	

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
	for i in xrange(159): #always 160 steps for total trip
		path_sum += arr[x][y]
		if x == 79: y += 1
		elif y == 79: x += 1
		else:
			if random() > .5: x += 1
			else: y += 1
	return path_sum


if __name__ == '__main__':
	import boilerplate, time
	boilerplate.all(time.time(),main())