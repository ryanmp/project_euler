import math
'''
By listing the set of RPFs for d <= 1,000,000 in ascending order of size,
find the numerator of the fraction immediately to the left of 3/7.

note:
RPF = reduced proper fraction (HCF of n,d == 1)
HCF = highest common factor
'''

'''
# Listing all of the fractions is slow. We can quickly come up with the right answer
# with just a little bit of math. see main().
from operator import itemgetter

def collect(l, index):
   return map(itemgetter(index), l)

def rpf_set(n):
	s = []
	# all possible fractions: n/d where n<d
	for i in xrange(1,n+1):
		for j in xrange(i+1,n+1):
			s.append((i,j))

	# reduced set where HCF(n,d)=1
	r = set([])
	x = []
	for i in s:
		temp = float(i[0])/i[1]
		if temp not in r:
			r.add(temp)
			x.append(i)
	return x

def ordered(n):
	new = []
	for i in n:
		temp = float(i[0])/i[1]
		new.append((temp,i))

	new.sort()
	return new

def left_of(s,(x,y)):
	idx = collect(s,1).index((x,y))
	return s[idx-1][1]
'''

def is_prime(n):
	for i in xrange(2,int(math.sqrt(n))+1):
		if n%i == 0:
			return False
	return True

# returns reduced fraction if possible, otherwise it returns False
def reduce_f(x,y):
	for i in xrange(int(y/2),2,-1):
		if x%i == 0:
			if y%i ==0:
				return x/i, y/i
	return False


def main():
	# the next 3 lines run the old method
	#x = rpf_set(1000) # all the reduced fractions... 8 -> 1e6 for final answer
	#y = ordered(x) # order them... now we have a list of tuples s.t. (real,(num,den))
	#return left_of(y,(3,7)) # which one comes right before 3/7 ?

	# the rest of these lines run the new 'method' ... it's just some basic math
	m = int(1000000/float(7)) #multiplier
	ret = reduce_f(m*3, m*7+1)
	if (ret):
		return ret[0]
	else:
		return m*3 # just return n

if __name__ == '__main__':
	import boilerplate, time
	boilerplate.all(time.time(),main()) # works but too slow as usual. I can do 1000... but not 1 000 000
