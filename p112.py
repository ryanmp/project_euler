'''

Working from left-to-right if no digit is exceeded by the digit to
its left it is called an increasing number; for example, 134468.

Similarly if no digit is exceeded by the digit to its right it is
called a decreasing number; for example, 66420.

We shall call a positive integer that is neither increasing nor
decreasing a "bouncy" number; for example, 155349.

Clearly there cannot be any bouncy numbers below one-hundred,
but just over half of the numbers below one-thousand (525) are
bouncy. In fact, the least number for which the proportion of
bouncy numbers first reaches 50% is 538.

Surprisingly, bouncy numbers become more and more common and by
the time we reach 21780 the proportion of bouncy numbers is equal to 90%.

Find the least number for which the proportion of bouncy numbers
is exactly 99%.

'''

def is_bouncy(n):
	digit_list = [int(i) for i in list(str(n))]
	not_increasing = 0
	not_decreasing = 0
	for i in xrange(0,len(digit_list)-1):
		curr = digit_list[i]
		next = digit_list[i+1]
		if (next > curr):
			#print 'not_decreasing'
			not_decreasing = 1
		if (next < curr):
			#print 'not_increasing'
			not_increasing = 1
		if (not_increasing and not_decreasing):
			return True
	return False

def main():
	max_n = 1917800
	num_bouncy = 0
	for n in xrange(1,max_n+1):
		if (is_bouncy(n)):
			num_bouncy += 1
		if (num_bouncy*1./max_n >= .9):
			return n

if __name__ == '__main__':
	import boilerplate, time
	boilerplate.all(time.time(),main())