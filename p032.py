'''
problem 32:
We shall say that an n-digit number is pandigital
if it makes use of all the digits 1 to n exactly once;
for example, the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 x 186 = 7254,
containing multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product
identity can be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be
sure to only include it once in your sum.

solution:
as usual... starting w/ a brute-force like solution - I'm generating
all 9-digit pandigital numbers first via permutations, 
then expanding this set by the dimension of all possible ways it can be
split into 3 substrings.

And then I have a list of ~ 10 million test cases. I lastly check the 
criterion for each of these, then add the solutions to a set, and return 
the sum of the set at the end.

All of this takes 2-3 minutes. 

Prior to rethinking the problem... I could first reduce the search
space quite a bit if I wanted to. I'll save that for another day.

'''

def is_pandigital(a,b,c):
	l = []
	l += list(str(a))
	l += list(str(b))
	l += list(str(c))

	true_test_case = [str(i) for i in xrange(1,10)]
	l.sort()
	if (l == true_test_case):
		return True
	else:
		return False
	
def satisfies_eq(a,b,c):
	if (a * b == c):
		return True
	else:
		return False

def solver():
	from itertools import permutations, combinations

	all_ps = list(permutations([str(i) for i in xrange(1,10)]))
	flattened_ps = []
	for ps in all_ps:
		flattened_ps.append(''.join(ps))

	all_ps_all_splits = []

	for f in flattened_ps:
		for i in xrange(1,9):
			for j in xrange(i+1,9):
				#print f[0:i], f[i:j], f[j:]
				all_ps_all_splits.append((f[0:i], f[i:j], f[j:]))

	solutions = set()
	
	for x in all_ps_all_splits:
		if satisfies_eq(int(x[0]),int(x[1]),int(x[2])):
			#if is_pandigital(x[0],x[1],x[2]):
			solutions.add(x[2])

	return sum([int(i) for i in solutions])

def main():
	return solver()

	



if __name__ == '__main__':
	import boilerplate, time
	boilerplate.all(time.time(),main())