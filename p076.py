''' counting sums 
explanation via example:
n == 5:

4 + 1
3 + 2
3 + 1 + 1
2 + 2 + 1
2 + 1 + 1 + 1
1 + 1 + 1 + 1 + 1

if sum == 5 -> there are 6 different combos
'''

def main():
	return 0

# how many different ways can a given number be written as a sum?
# note: combinations, not permutations
def count_sum_reps(n):
	''' my gut tells me that this can be formulated as a math problem...
	let's first see if we can detect the pattern:

	1 -> 1
	2 -> 1
	3 -> 1+2,
		 1+1+1: 2
	4 -> 1+3,
		 2+2,2+1+1,
		 1+1+1+1: 4
	5 -> 6
	6 -> 	5+1,
			4+2, 4+1+1,
			3+3, 3+2+1, 3+1+1+1,
			2+2+2, 2+2+1+1, 2+1+1+1+1,
			1+1+1+1+1+1 : 10
	7 ->	6+1
			5+2 5+1+1
			4+3 4+2+1 4+1+1+1
			3+3+1 3+2+2 3+2+1+1 3+1+1+1+1
			2+2+2+1 2+2+1+1+1 2+1+1+1+1+1
			(7x)+1
			: 14

	8 ->	7+1
			6+2 6+1+1
			5 = "3"
			4 = "4"
			3+3+2 3+3+1+1 3+2+2+1 3+2+1+1+1 3+(5x)+1 "5"
			2+2+2+2 ... "4"
			"1"
			: 19

	9 ->	 

	yikes, I'm seeing the emergence of a pattern, n-1 rows. growing by +1
	descending.. until it reaches the corner,
	but i would need to do several more in order to see the pattern on the bottom
	rows (after the corner), assuming there is a pattern

	'''

	return 'not finished yet'



if __name__ == '__main__':
	import boilerplate, time
	boilerplate.all(time.time(),main())
