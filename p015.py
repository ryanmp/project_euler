from itertools import permutations, combinations
from math import factorial as f
def main(): # how many lattice-routes (right, down) are there through a 20x20 grid?
	
	n = (20,20)
	path_length = n[0]

	'''
	# n! ouch!
	one_route = [0 for i in xrange(n[0])] + [1 for i in xrange(n[0])] # one-route right:0, down:1
	all_routes = set(list(permutations(one_route)))
	return len(all_routes)
	
	# this method assumes symmetry for grid
	# calculating combinations is much faster than permutations... like n^2 ?
	return len(list(combinations(range(path_length*2),path_length)))
	'''

	# I think we can do better...
	# oh duh... we don't need a list of all the paths,
	# just get the number -> use math:
	# n! / ( r! (n - r)! )
	n = path_length*2
	r = path_length
	ret = f(n)/( f(r) * f(n-r) )
	return ret

if __name__ == '__main__':
	import boilerplate, time, resource
	t = time.time()
	r = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
	boilerplate.all(main(), t, r)

