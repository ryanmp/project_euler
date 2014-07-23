from random import randint
from itertools import permutations

'''
What is the probability that Pyramidal Pete beats Cubic Colin?
Give your answer rounded to seven decimal places in the form 0.abcdefg
'''

def main():
	print pete_wins_prob(5000) # should be close...
	print pete_better_than_e_value_prob()
	print pete_wins(1000) # would work if n could equal 6**6
	return 'not finished yet'

def pete_sum():
	return sum([randint(1,4) for i in xrange(9)])

def colin_sum():
	return sum([randint(1,6) for i in xrange(6)])

'''
attempt #1:
trying to determine it stochastically

note: it looks like aren't going to get the desired level of
precision in a reasonable amount of time
'''
def pete_wins_prob(num_trials):
	wins = 0
	for i in xrange(num_trials):
		if pete_sum() > colin_sum(): wins += 1
	return float(wins)/num_trials


'''
attempt #2:
what if we use the expected value for one, and then check to see how many
of the possible sums for the other are above and below this expected value?

note: the result is highly dubious as it isn't very close to attempt #1
'''
def pete_better_than_e_value_prob():

	colin_expected_value = sum([i for i in xrange(1,7)])
	num_pete_possible_sums = 4**9

	dice = []
	for i in xrange(9):
		dice += [1,2,3,4]
	p = permutations(dice,9) # all possible results for pete

	wins = 0
	for i in xrange(num_pete_possible_sums):
		this_sum = sum(next(p))
		if this_sum > colin_expected_value: wins += 1

	return float(wins)/num_pete_possible_sums

'''
attempt #3:
like in #2, I could enumerate all the permutations for pete & colin,
and then compare all of these sums...
this would yield the correct answer, but this is likely unfeasible
in a timely manner
'''
def pete_wins(n):

	dice = []
	for i in xrange(9):
		dice += [1,2,3,4]
	p = permutations(dice,9) # all possible results for pete

	dice = []
	for i in xrange(6):
		dice += [1,2,3,4,5,6]
	c = permutations(dice,6) # all possible results for colin

	wins = 0
	for i in xrange(n):
		pete_score = sum(next(p))
		for j in xrange(n): # smaller range for testing
			colin_score = sum(next(c))
			if pete_score > colin_score: wins += 1

	print float(wins)/(n**2)


if __name__ == '__main__':
	import boilerplate, time
	boilerplate.all(time.time(),main())