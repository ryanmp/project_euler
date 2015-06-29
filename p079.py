'''
A common security method used for online banking is to
ask the user for three random characters from a passcode.
For example, if the passcode was 531278, they may ask for
the 2nd, 3rd, and 5th characters; the expected reply would be: 317.

The text file contains fifty successful login attempts.

Given that the three characters are always asked for in order,
analyse the file so as to determine the shortest possible secret
passcode of unknown length.
'''

def main():

	# grab text file of login attempts
	attempts = [i[:3] for i in open('p79.in').read().split('\n')] #file -> list

	'''
	method:
	let's start by creating a list of sets for which numbers
	come before and after each integer we might encounter:
	'''
	before = [set([]) for i in xrange(0,10)] #0-9
	after = [set([]) for i in xrange(0,10)] #0-9
	for i in attempts:
		idx = int(i[0])
		after[idx].add(int(i[1]))
		after[idx].add(int(i[2]))
		idx = int(i[1])
		before[idx].add(int(i[0]))
		after[idx].add(int(i[2]))
		idx = int(i[2])
		before[idx].add(int(i[0]))
		before[idx].add(int(i[1]))

	'''
	now we can check to see if a given number has something in its 
	'after' set but nothing in its 'before' set...
	this would mean that number must come first. 
	then we remove that number from all our sets, and repeat for as long
	as necessary to find the complete password
	'''
	ans = []
	while (True):

		# if a given entry has contents in the 'after' set but not in the 
		# 'before' set...
		done = True
		for i,j,n in zip(before,after,[i for i in xrange(len(before))]):
			if len(i) == 0 and len(j) != 0 and n not in ans:
				done = False
				ans.append(n)

		 # didn't find another.. assuming we are finished!
		if (done):
			return join_ints(ans)

		# remove ans from our sets
		for i,j in zip(before,after):
			i -= set([ans[-1]])
			j -= set([ans[-1]])

def join_ints(l):
	l = [str(i) for i in l] # to array of chars
	as_str = ''.join(l)
	return int(as_str)

if __name__ == '__main__':
	import boilerplate, time
	boilerplate.all(time.time(),main())