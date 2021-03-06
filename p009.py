def main(): #return product (a*b*c) of pythagorean triple (s.t. a + b + c = 1000)
	for a in xrange(1,332):
		for b in xrange(a,499):
			c = 1000-a-b
			if a<b and b<c and a+b+c==1000:
				if is_pyth_triple(a,b,c):
					return a*b*c

def is_pyth_triple(a,b,c):
	return (a*a + b*b == c*c)	

if __name__ == '__main__':
	import boilerplate, time, resource
	t = time.time()
	r = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
	boilerplate.all(main(), t, r)
