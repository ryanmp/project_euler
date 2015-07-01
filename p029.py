'''

How many distinct terms are in the sequence generated
by a^b for 2 <= a <= 100 and 2 <= b <= 100?


'''

def main(): 
	s = set()
	l = 100
	for i in xrange(2,l+1):
		for j in xrange(2,l+1):
			next_term = i**j
			s.add(next_term)
	return len(s)


if __name__ == '__main__':
	import boilerplate, time
	boilerplate.all(time.time(),main())
