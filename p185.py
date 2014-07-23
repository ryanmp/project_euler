'''
my hillclimb for this one kind of sucks....
I don't know what sort of function to use for simulated annealing

'''

import random, sys, math

def main():
	return 0

# input: 	guess, 16-digit int as a string
#			data, a list of previous guesses with responses
def check_answer(guess, data):
	assert(len(guess)==16)
	for i in data:
		diff = num_correct(i[0],guess) - i[1]
		if (diff == 0):
			print 'passes',i
		else:
			print 'fails:',i,'by:',diff
		
# a derivative of 'check_answer()' that gives a score for how close our
# guess is
def rate_answer(guess, data):
	val = 0
	for i in data:
		diff = math.fabs(num_correct(i[0],guess) - i[1])
		if diff>0:
			val += diff
	return val

# returns how many digits x and y have in common
# (assuming they are the same length!)
def num_correct(x,y):
	assert(len(x)==len(y))
	ret = 0
	for i,j in zip(x,y):
		if i==j: ret += 1
	return ret

def mod_guess(guess,idx,new):
	#r = str(random.randint(0,9))
	r = new
	new_guess = guess[:idx] + r + guess[idx+1:]
	return new_guess




# get input data (it's a list of guesses.. with the mastermind reponses)
lines = [i for i in open('p185.in').read().split('\n')]
data = []
for i in lines:
	tmp = i.split(' ')
	data.append((tmp[0],int(tmp[1][1:2])))

# example of how to use my functions
r = str(random.randint(1000000000000000, 9999999999999999)) 
print 'a guess...', r
#check_answer(r, data)
#print rate_answer(r,data)

# hill climb w/ simulated annealing
'''
temp = 1000
x = 1
for n in xrange(1,200): # decreasing temp
	x += n
	for m in xrange(2): # reps per temp
		for i in xrange(16): # rotate through each val
			original_val = rate_answer(r,data)
			new_guess = mod_guess(r,i,str(random.randint(0,9)))
			new_val = rate_answer(new_guess,data)
			if new_val < original_val + temp*50*(random.random()-.5)/(temp*x): # temp=simulating annealing
				
				print new_val, new_guess, temp*50*(random.random()-.5)/(temp*x)
				r = new_guess
				original_val = new_val
'''


# another hill climb... doing a full rotation for each digit now...
best_val = sys.maxint
for rotation in xrange(30):
	for which_digit in xrange(16):
		for idx in xrange(10):
			new_guess = mod_guess(r,which_digit,str(idx))
			new_val = rate_answer(new_guess,data)
			if new_val < best_val:
				print new_guess, new_val # just print improvements
				best_val = new_val
				best_guess = new_guess
	r = best_guess # keeping the best guess from digit rotation
print best_val, best_guess


if __name__ == '__main__':
	import boilerplate, time
	boilerplate.all(time.time(),main())