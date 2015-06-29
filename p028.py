def main(_in): #number spiral diagonals

	_max = _in+_in # calculating number of elements from dimensions

	l = [1] # list of the diagonal elements 
	i = l[0] # starting point
	add_amount = 0

	n = 1 # number of elements so far
	while (True):
		add_amount += 2

		cycle_counter = 4 # each cycle adds four new elements
		while (cycle_counter > 0):
			n += 1
			if n>=_max:
				return sum(l) # if the last element gets us to the end... return!
			i += add_amount
			l.append(i)
			cycle_counter -= 1

if __name__ == '__main__':
	import boilerplate, time
	boilerplate.all(time.time(),main(1001))
