'''

coin sums (british version):

coin values:
1p, 2p, 5p, 10p, 20p, 50p, (100p) and (200p)

how many different ways can we get to 200p (using any number of coins)?

------

my solutions:
basically just brute force with a couple of tweaks to speed things up
if this problem was just a bit larger, I'd need a smarter algo.


'''

def main(): 
	t = 0
	for g in xrange(0,1):
		for f in xrange(0,3):
			for e in xrange(0,9):
				for d in xrange(0,19):
					for c in xrange(0,39):
						for b in xrange(0,99):
							for a in xrange(0,199):
								total = a*1 + b*2 + c*5 + d*10 + e*20 + f*50 + g*100
								if (total == 200):
									t += 1
									break
								if (total > 200):
									break
	return t + 8 # don't forget solutions w/ using just all of one coin 

if __name__ == '__main__':
	import boilerplate, time
	boilerplate.all(time.time(),main())
