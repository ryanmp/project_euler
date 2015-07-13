'''
Find the unique positive integer whose square has the form 1_2_3_4_5_6_7_8_9_0,
where each "_" is a single digit

solution:
in progress

todo:
hm... So far I've realized that it takes too long to generate
all 1 billion possible solutions... prior to even checking them. 
I'll return to this one at a later date.

'''

# generate possible solutions

all_permutations = []
for i in xrange(0,999999+1):
	l = len(str(i))
	this_sol = ''
	for padding in xrange(3-l):
		this_sol += '0'
	this_sol += str(i)
	all_permutations.append([int(x) for x in list(this_sol)])

print len(all_permutations)

# check possible solutions

i = 0
for var_digits in all_permutations:
	set_digits = [1,2,3,4,5,6,7,8,9,0]
	result = ''
	for d in xrange(0,len(set_digits)):
		if (d < len(set_digits) - 1):
			result += str(set_digits[d]) + str(var_digits[d])
		else:
			result += str(set_digits[d])

	ans = math.sqrt(int(result))
	#print ans
	if (ans % 1 == 0):
		print '-----', ans 
	i += 1
	if i > 1000:
		break

def main():
	return 'TBI'

if __name__ == '__main__':
	import boilerplate, time
	boilerplate.all(time.time(),main())