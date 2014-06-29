from itertools import permutations, combinations
def main(n): # how many lattice-routes (right, down) are there through a 20x20 grid?
	
	'''
	# n! ouch!
	one_route = [0 for i in xrange(n[0])] + [1 for i in xrange(n[0])] # one-route right:0, down:1
	all_routes = set(list(permutations(one_route)))
	return len(all_routes)
	'''
	# this method assumes symmetry for grid
	# calculating combinations is much faster than permutations... like n^2 ?
	path_length = n[0]
	return len(list(combinations(range(path_length*2),path_length)))

if __name__ == '__main__':
	import boilerplate, time
	boilerplate.all(time.time(),main((10,10)))

