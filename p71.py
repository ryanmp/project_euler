'''
rpf = reduced proper fraction
note: HCF = highest common factor... so basically that each fraction is fully reduced
'''

from operator import itemgetter

def collect(l, index):
   return map(itemgetter(index), l)

def rpf_set(n):
	s = []
	# all possible fractions (n,d)
	for i in xrange(1,n+1):
		for j in xrange(i,n+1):
			s.append((i,j))

	# reduced set
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




def main():
	x = rpf_set(8) # all the reduced fractions... 8 -> 1e6 for final answer
	y = ordered(x) # order them... now we have a list of tuples s.t. (real,(num,den))
	return left_of(y,(3,7)) # which one comes right before 3/7 ?


if __name__ == '__main__':
	import boilerplate, time
	boilerplate.all(time.time(),main()) # works but too slow as usual. I can do 1000... but not 1 000 000
