'''
A 30x30 grid of squares contains 900 fleas, initially one flea per square.
When a bell is rung, each flea jumps to an adjacent square at random
(usually 4 possibilities, except for fleas on the edge of the grid or
at the corners).

What is the expected number of unoccupied squares after 50
rings of the bell? Give your answer rounded to six decimal places.
'''

from random import choice

def main():
	# how many trials would we need to get 6-decimal precision? QUITE A FEW!
	# we may need a more mathematical approach...
	print run_trials(7) 
	return 'not finished'

def random_jump(flea):
	possible_jumps = []
	if flea[0] != 0:  possible_jumps += [0]
	if flea[1] != 0:  possible_jumps += [1]
	if flea[0] != 29:  possible_jumps += [2]
	if flea[1] != 29:  possible_jumps += [3]
	which_jump = choice(possible_jumps)
	if (which_jump == 0): flea = (flea[0]-1,flea[1])
	if (which_jump == 1): flea = (flea[0],flea[1]-1)
	if (which_jump == 2): flea = (flea[0]+1,flea[1])
	if (which_jump == 3): flea = (flea[0],flea[1]+1)
	return flea

def bell_rings(fleas,n):
	for i in xrange(n):
		for i in xrange(len(fleas)):
			fleas[i] = random_jump(fleas[i])
	return fleas

def num_empty(fleas):
	return 900-len(set(fleas))

def run_trials(n):
	expected_value = 0
	for i in xrange(n):
		# init array of fleas
		fleas = []
		for i in xrange(30):
			for j in xrange(30):
				fleas.append((i,j))

		fleas = bell_rings(fleas,50)
		expected_value += num_empty(fleas)

	return float(expected_value)/n

if __name__ == '__main__':
	import boilerplate, time
	boilerplate.all(time.time(),main())
