'''

problem:
--------

A number chain is created by continuously adding the square of
the digits in a number to form a new number until it has been
seen before.

For example,

44 -> 32 -> 13 -> 10 -> 1 -> 1
85 -> 89 -> 145 -> 42 -> 20 -> 4 -> 16 -> 37 -> 58 -> 89

Therefore any chain that arrives at 1 or 89 will become stuck
in an endless loop. What is most amazing is that EVERY starting
number will eventually arrive at 1 or 89.

How many starting numbers below ten million will arrive at 89?

solution:
---------

Works, but slow. Will look into optimization next.

'''

def get_next(x):
	l = list(str(x))
	l = [int(i) for i in l]
	l_sum = 0
	for n in l:
		l_sum += n**2
	return l_sum

def run_loop(n):
	if (n == 1):
		return 0
	if (n == 89):
		return 1
	n = get_next(n)
	return run_loop(n)

def main():
	max_n = int(10e6) # goal
	max_n = 9000 # smaller version
	solutions = 0
	for i in xrange(1,max_n):
		solutions += run_loop(i)
	return solutions

if __name__ == '__main__':
	import boilerplate, time
	boilerplate.all(time.time(),main())
	