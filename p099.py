'''

Comparing two numbers written in index form like 2^11 and 3^7 is not difficult, as any calculator would confirm that 2^11 = 2048 < 3^7 = 2187.

However, confirming that 632382^518061 > 519432^525806 would be much more difficult, as both numbers contain over three million digits.

Using base_exp.txt (right click and 'Save Link/Target As...'), a 22K text file containing one thousand lines with a base/exponent pair on each line,
determine which line number has the greatest numerical value.

'''

import math

def main():

	lines = open('p099.in').read().split('\n')

	best_line_idx = -1
	biggest_number = 0

	for (idx,line) in enumerate(lines):
		d = line.split(',')
		pairs.append((int(d[0]),int(d[1])))
		base = math.log(int(d[0]))
		exp = int(d[1])
		number = base * exp
		if number > biggest_number:
			best_line_idx = idx+1 # start numbering lines at 1
			biggest_number = number

	return best_line_idx

if __name__ == '__main__':
	import boilerplate, time
	boilerplate.all(time.time(),main())
