def main(n): # Evaluate the sum of all the amicable numbers under 10000
	amicable_numbers = []
	for i in xrange(1,n):
		a = proper_divisors(i)
		b = proper_divisors(sum(a))
		if sum(b) == i and sum(a) != sum(b):
			amicable_numbers.append(i)
	return sum(amicable_numbers)

def proper_divisors(n):
	ret = []
	for i in xrange(1,int(n/2)+1):
		if n%i == 0:
			ret.append(i)
	return ret

'''
# unnecessary - this may be clearer conceptually, but it's replacement
# in main() is faster
def is_amicable_pair(a,b):
	if sum(proper_divisors(a)) == b:
		if sum(proper_divisors(b)) == a:
			return True
	return False
'''

if __name__ == '__main__':
	import boilerplate, time
	boilerplate.all(time.time(),main(10000))