'''
Spiral Primes

the first part (and the hardest part) will be to layout numbers
in a spiral within a 2d array

ok, almost there.

I can search for the proper range for the dimensions...
and will eventually narrow it down. But my algo is too slow.
I wonder if I use a simple isprime foo instead of generating all the primes
in my grid... and then just check the diagonals.
That might be quicker than my current approach.

'''

from collections import deque
import numpy as np

def maxItemLength(a):
    maxLen = 0
    rows = len(a)
    cols = len(a[0])
    for row in xrange(rows):
        for col in xrange(cols):
            maxLen = max(maxLen, len(str(a[row][col])))
    return maxLen

def print2dList(a):
    if (a == []):
        # So we don't crash accessing a[0]
        print []
        return
    rows = len(a)
    cols = len(a[0])
    fieldWidth = maxItemLength(a)
    print "[ ",
    for row in xrange(rows):
        if (row > 0): print "\n  ",
        print "[ ",
        for col in xrange(cols):
            if (col > 0): print ",",
            # The next 2 lines print a[row][col] with the given fieldWidth
            format = "%" + str(fieldWidth) + "s"
            print format % str(a[row][col]),
        print "]",
    print "]"

def create_spiral_array(d):
	dimensions = d # x == y (square grid) where x is odd

	l = [i for i in xrange(1,dimensions**2+1)]
	arr = [[0 for i in xrange(dimensions)] for i in xrange(dimensions)]
	idx = {'x':dimensions/2,'y':dimensions/2}
	directions = deque([(0,1),(-1,0),(0,-1),(1,0)], maxlen=4) #right, up, left, down (x,y)

	num_steps = 1
	inc_every_two = 0
	i = 0
	while i < dimensions**2:
		
		curr_dir = directions[0]

		#print 'curr_dir ', curr_dir
		
		counter = 0 # count up to num steps then reset and cycle direction
		while (counter < num_steps): # moving some number of steps in a single direction
			#print idx
			arr[idx['x']][idx['y']] = l[i]
			#print2dList(arr)
			i += 1
			idx['x'] += curr_dir[0] # move in x
			idx['y'] += curr_dir[1] # move in y
			counter += 1

		directions.rotate(-1) # pointing in a new direction

		inc_every_two += 1
		if (inc_every_two > 1):
			inc_every_two = 0
			num_steps += 1

	return arr

def primesfrom2to(n):
    # http://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188
    """ Input n>=6, Returns a array of primes, 2 <= p < n """
    sieve = np.ones(n/3 + (n%6==2), dtype=np.bool)
    sieve[0] = False
    for i in xrange(int(n**0.5)/3+1):
        if sieve[i]:
            k=3*i+1|1
            sieve[      ((k*k)/3)      ::2*k] = False
            sieve[(k*k+4*k-2*k*(i&1))/3::2*k] = False
    return np.r_[2,3,((3*np.nonzero(sieve)[0]+1)|1)]


# slower
def is_prime(n):
	for i in xrange(2,n-1,1):
		if (n%i == 0):
			return False
	return True


def main():

	
	for x in xrange(18901,18905,2): # manually searching for the correct dimensional range

		dimensions = x

		#spiral_arr = create_spiral_array(dimensions)
		#print2dList(spiral_arr)
		arr = gen_seq(x)

		num_of_diagonals = dimensions*2 - 1
		num_of_prime_diagonals = 0

		primes = set(primesfrom2to(dimensions**2))
		'''
		for i in xrange(dimensions):
			if spiral_arr[i][i] in primes:
				num_of_prime_diagonals += 1
			if spiral_arr[dimensions-1-i][i] in primes:
				num_of_prime_diagonals += 1
				'''
		
		for i in arr:
			if i in primes:
				num_of_prime_diagonals += 1


				

		print dimensions, (num_of_prime_diagonals*1.0/num_of_diagonals)*100	
	



	return "TBI"






# generate sequence

def gen_seq(dims):
	l = [1]
	inc_amount = 2
	new_cycle_add = 2
	#dims = 7 # must be odd
	for i in xrange(0,dims/2):
		for j in xrange(0,4):
			l.append(l[-1] + inc_amount)
		inc_amount += new_cycle_add

	return l




if __name__ == '__main__':
	import boilerplate, time
	boilerplate.all(time.time(),main())
