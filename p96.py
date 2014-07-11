# solving sodoku - hooray!
# I'm guessing this will be a search problem...
import numpy

def main(): 

	f = open('p96.in')
	all_games = format_input(f)
	g = numpy.array(all_games[0]) # just the first game

	print 'is it valid?', valid_game(g)
	#pretty_print(g)
	m = get_all_moves(g)
	num_moves = [len(i) for i in m]
	# next... generate new array out of all the ones in the num_moves array
	# this may work be because now we have more cells fully determined than when we
	# began
	# this approach will only work if each step adds at least 1 fully determined cell
	# otherwise we will need to turn it into a search problem

	return 0


# input: raw file
# output: an array of games
def format_input(file):
	f = file.read().split('\n')
	games = [] # a list of games... each entry is 9x9 2d list
	for i in xrange(len(f)/10):
		game = f[i*10:(i+1)*10]
		game = game[1:10] # cut off 'grid' text
		formatted_game = []
		for line in game:
			line = [int(i) for i in list(line)]
			formatted_game.append(line)
		games.append(formatted_game)
	return games


# basic Node class... used to create tree structure
class Node:
	def __init__(self, data, parent=None):
		self.data = data
		self.children = []
		self.parent = parent
		# to be set via heuristic f() in a* algo
		self.heuristic_value = 0 

	def add_child(self, obj):
		self.children.append(obj)
		#the last child is the one just added
		self.children[-1].parent = self 

	# used primarly for testing purposes
	def print_tree(self, idx=0):
		idx += 1
		if (self):
			print idx; print self.data
			for i in self.children:
				i.print_tree(idx)


def pretty_print(game):
	for i in game: print i

def valid_set(s_in):
	s = list(s_in.flatten()) #numpy.array -> list
	for i in s:
		if (s.count(i) > 1 and i != 0):
			return False
	return True	

def valid_game(game):
	#rows & cols
	for i in xrange(9):
		if not valid_set(game[i,:]): return False
		if not valid_set(game[:,i]): return False
	#the other 9 grids...
	for i in xrange(3):
		for j in xrange(3):
			if not valid_set( game[i*3:(i+1)*3:,j*3:(j+1)*3] ):
				return False
	return True

# input: x,y, coordinates
# output: a list of possible moves for this location
def get_moves(x,y,game):
	assert(game[x][y]) == 0 #precondition: must be an undetermined location
	l = set([i for i in xrange(1,10)]) #all possibilities, 1-9
	l = l - set(game[x,:]) # remove repeats in row
	l = l - set(game[:,y]) # remove repeats in column
	small_grid = game[x*3:(x+1)*3:,y*3:(y+1)*3]
	flat = [x for sublist in small_grid for x in sublist] #flatten 2d array
	l = l - set(flat) # remove repeats in sub-grid
	return l

#input: a game with unknown spots
#output: list of possible moves for each location
def get_all_moves(game):
	moves = []
	for x in xrange(9):
		for y in xrange(9):
			if game[x][y] == 0:
				m = get_moves(x,y,game)
			else:
				m = [game[x][y]]
			moves.append(m)
	return moves

if __name__ == '__main__':
	import boilerplate, time
	boilerplate.all(time.time(),main())



