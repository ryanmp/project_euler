'''
Diophantine reciprocals

1/x + 1/y = 1/n
for n = 4... there are 3 solutions...

what is the smallest value of n that has over 1000 solutions?

'''


def is_solution(x,y,n):
	if 1.0/x + 1.0/y == 1.0/n:
		return True
	else:
		return False

def num_solutions(n):
	my_range = int(1/(1./n - 1./(n+1)))
	num_solutions = 0
	for x in xrange(n+1,n*2+1):
		for y in xrange(x,my_range+1):
			if is_solution(x,y,n):
				print x,y,n
				num_solutions += 1
	return num_solutions

def main():

	# cranks up xrange upper limit...
	# and this would find teh solution.... eventually
	for n in xrange(2,20):
		print num_solutions(n)

	return 'not-finished yet'

if __name__ == '__main__':
	import boilerplate, time
	boilerplate.all(time.time(),main())
