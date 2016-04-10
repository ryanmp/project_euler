'''
my hillclimb for this one kind of sucks....
I don't know what sort of function to use for simulated annealing

'''


from __future__ import print_function
import random, sys, math
import time
import datetime


# a derivative of 'check_answer()' that gives a score for how close our
# guess is... a score of zero would mean that our guess passes all the test cases (is correct)
def rate_answer(guess, data):
	val = 0
	for i in data:
		diff = abs(num_correct(i[0],guess) - i[1])
		val += diff
	return val

# returns how many digits x and y have in common
def num_correct(x,y):
	assert(len(x)==len(y))
	ret = 0
	for i,j in zip(x,y):
		if i==j: ret += 1
	return ret

def mod_guess(guess,idx,new):
	#r = str(random.randint(0,9))
	new_guess = guess[:idx] + str(new) + guess[idx+1:]
	return new_guess


def lerp(t, x, y):
# t is from interval <0, 1>
    return (1 - t) * x + t * y



# 1 9646041578846586
# 1 4640560908628538
# 1 4242291570916534
# 1 9446561549526576
# 1 4640590513814578
# 1 5091890491088537
# 0 4640261571849533 !!!

'''
trial 19 starting w/ 9090428905556607 2016-04-03 16:48:07
._2.0_-1-== 22 22 0482487994920236 -0.383537869764 1 ==
== 20 20 1482487994920236 1.19532136816 1 ==
== 19 19 7082487994920236 0.391575367055 1 ==
== 18 18 7282487994920236 1.25537820689 1 ==
== 16 16 7642487994920236 1.54411221376 1 ==
== 15 15 7644487994920236 0.812265716875 1 ==
== 14 14 7644587994920236 1.35340049804 1 ==
== 11 11 7644807994920236 1.32637387308 1 ==
== 9 9 7644807974920232 0.19357144494 1 ==
== 8 8 5644800978920133 1.01085506064 1 ==
== 7 7 0644800978920533 -0.549341440452 1 ==
== 6 6 7644800978920533 1.6960489372 1 ==
._1.978_-1-== 5 5 7644660071620513 -0.440200437228 1 ==
== 4 4 7644261571640513 0.116576646616 1 ==
== 3 3 7640261571640513 1.82645799219 1 ==
._1.956_-1-._1.934_-2-== 2 2 0640261571640533 -0.377500277138 2 ==
._1.912_-2-._1.89_-2-== 1 1 4640261571845533 0.536897642968 2 ==
r._1.868_-2-._1.846_-2-r._1.824_-2- found solution !!!
answer: 4640261571849533
time: 136.273121119



1.84 2 14 3 9
1.8 2 13 1 8
2.24 1 6 0 4
2.24 1 6 1 5
2.23 1 5 0 8 53
1.97 1 8 0 8 26
2.13333333333 2 15 0 2

'''


'''
lines = [i for i in open('p185.in').read().split('\n')]
data = []
for i in lines:
	tmp = i.split(' ')
	data.append((tmp[0],int(tmp[1][1:2])))

r = str(9999999999999999) 
x = mod_guess2(r, data, 4)
print(r, x, len(r), len(x))
'''

def mod_guess2(guess, data, idx):
	num_matches = data[idx][1]
	idxs_to_pick = random.sample(set([i for i in xrange(0,15)]), num_matches)
	for i in idxs_to_pick:
		guess = mod_guess(guess,i,data[idx][0][i]) 
	return guess

def main():

	# get input data (it's a list of guesses.. with the mastermind reponses)
	lines = [i for i in open('p185.in').read().split('\n')]
	data = []
	for i in lines:
		tmp = i.split(' ')
		data.append((tmp[0],int(tmp[1][1:2])))

	# who knows how many trials might actually be required to arrive at a solution
	for i in xrange(10):

		ts = time.time()
		st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

		r = str(random.randint(1000000000000000, 9999999999999999)) 
		print("trial", i, "starting w/", r, st)
		x = hill_climb(r,data)
		if x != -1:
			return x

	return -1
	
def hill_climb(r,data):

	#r = str(random.randint(1000000000000000, 9999999999999999)) 

	#r = '9090428905556607'

	best_so_far = 1000

	best_guess = r

	next_num_mods = 1

	num_temp_intervals = 100

	for n in xrange(num_temp_intervals): 

		sys.stdout.write('.')
		sys.stdout.flush()

		temperature = lerp(n/(num_temp_intervals*1.0),3,1.0) # 2 -> 0.5

		#sys.stdout.write("_" + str(temperature) + "_")
		#sys.stdout.write("-" + str(max_num_mods) + "-")

		for m in xrange(300): # reps per temp #1000

			i = random.randrange(0,22)

			original_val = rate_answer(r,data)
			new_guess = r

			new_guess = mod_guess2(new_guess,data,i)

			new_val = rate_answer(new_guess,data)

			if new_val <= 0:
				print(" found solution !!!")
				print(temperature, i, m)
				return new_guess

			else:
				uncertainty = random.uniform(-1.0, 1.0)*temperature
				if new_val < best_so_far + uncertainty: # temperature=simulating annealing
					#sys.stdout.write('('+str(new_val)+')')
					r = new_guess
					original_val = new_val
					if new_val < best_so_far:
						best_so_far = new_val
						best_guess = new_guess
						#print("==", new_val, best_so_far, new_guess, uncertainty, next_num_mods, "==")

					#if new_val < 4:
					#print("==", new_val, best_so_far, new_guess, uncertainty, next_num_mods, "==")


	print("++", best_so_far, best_guess, "++")
	return -1



if __name__ == '__main__':
	import boilerplate, time
	boilerplate.all(time.time(),main())