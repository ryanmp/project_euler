# solving sodoku - hooray!
# I'm guessing this will be a search problem...
import numpy

def main(): 
	return 0

f = open('p96.in').read().split('\n')

games = [] # a list of games... each entry is 9x9 2d list
for i in xrange(len(f)/10):
	game = f[i*10:(i+1)*10]
	game = game[1:10] # cut off 'grid' text
	formatted_game = []
	for line in game:
		line = [int(i) for i in list(line)]
		formatted_game.append(line)
	games.append(formatted_game)

def pretty_print(game):
	for i in game: print i

def valid_set(s_in):
	s = list(s_in.flatten()) # numpy.array -> list
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

g = numpy.array(games[0])
# perform valid_game on numpy arrays...


if __name__ == '__main__':
	import boilerplate, time
	boilerplate.all(time.time(),main())