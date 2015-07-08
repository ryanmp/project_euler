'''

It turns out that 12 cm is the smallest length of wire that can be bent
to form an integer sided right angle triangle in exactly one way, but
there are many more examples.

12 cm: (3,4,5)
24 cm: (6,8,10)
30 cm: (5,12,13)
36 cm: (9,12,15)
40 cm: (8,15,17)
48 cm: (12,16,20)

In contrast, some lengths of wire, like 20 cm, cannot be bent to form
an integer sided right angle triangle, and other lengths allow more
than one solution to be found; for example, using 120 cm it is possible
to form exactly three different integer sided right angle triangles.

120 cm: (30,40,50), (20,48,52), (24,45,51)

Given that L is the length of the wire, for how many values of
L <= 1,500,000 can exactly one integer sided right angle triangle
be formed?

solution:

this would theoretically work... but it's too much work.
here's my current algo:
1. construct a set of all possible a+b+c = L, for L in 3 to 1.5e6
2. check if each of these a,b,c combos can construct a right triangle
3. if just one a,b,c combo can do this, then increment our return value

and here's what I'm thinking for an improvement:
1. generate a list of all right triangles (a,b,c) from 1 to n
   where a,b,c <= n
2. ??


notes:
here's another useful tool which I'm going to make
(in the spirit of boilerplate)
for a self container function which only requires a single input of some integer (n)
it'll run the function multiple times in a range (min,max)...
then print out a graph of the complexity





'''
from math import factorial
import boilerplate, complexity, time, random

def main():
	#boilerplate.all(time.time(),solver_one(200))
	#boilerplate.all(time.time(),solver_two(200))
	reload(complexity)

	complexity.run(solver_two,minn=3,maxn=200,num_samples=10)
	
# simplifying the process a bit...
# this is currently returning a diff value than solver_one... so I'll 
# need to add some output to determine why
def solver_two(max_l):
	lengths_with_one_solution = 0
	for length in xrange(3,max_l):
		if (check_length(length)):
			lengths_with_one_solution += 1
		

	return lengths_with_one_solution

def check_length(length):
	how_many_of_this_l = 0
	for i in xrange(1,length-1):
		for j in xrange(i,length-i):
			if is_right_triangle((i,j,length-i-j)):
				#print length, i, j, length-i-j
				how_many_of_this_l += 1
				if (how_many_of_this_l > 1):
					return False

	if (how_many_of_this_l == 1):
		return True
	else:
		return False

def solver_one(max_l):
	right_triangles = []
	how_many_values_of_L = 0
	for n in xrange(3,max_l):	
		combo_set = all_possible_combos(n)
		num_right_tris = 0
		for combo in combo_set:
			if is_right_triangle(combo):
				this_combo = combo
				num_right_tris += 1

		# only want to add lengths with just one possible right triangle		
		if (num_right_tris == 1):
			how_many_values_of_L += 1
			#right_triangles.append(this_combo)
			
	return how_many_values_of_L

# returns a set of tuples (a,b,c) where a+b+c = length
def all_possible_combos(length):
	s = set()
	for i in xrange(1,length-1):
		for j in xrange(1,length-i):
			#print i,j,length-i-j
			l = [i,j,length-i-j]
			l.sort()
			s.add(tuple(l))
	return s

# pass in lengths of all 3 sides
def is_right_triangle((a,b,c)):
	ret = False
	if (a**2 + b**2 == c**2):
		ret = True
	#print a,b,c, ' is ', ret 
	return ret

if __name__ == '__main__':
	'''
	import boilerplate, time
	boilerplate.all(time.time(),main())
	'''
	main()
	print 'TBI'