'''
The 5-digit number, 16807=7^5, is also a fifth power.
Similarly, the 9-digit number, 134217728=8^9, is a ninth power.

How many n-digit positive integers exist which are also an nth power?
'''

from math import pow

def main():
	solutions = 0
	for base in range(1, 10):
	    for power in range(1, 22):

	        val = int(pow(base, power))
	        num_digits = digit_count(val)

	        if num_digits == power:
	            solutions += 1

	        if num_digits > power:
	            break 

	return solutions


def digit_count(n):
	return len(str(n))


if __name__ == '__main__':
	import boilerplate, time
	boilerplate.all(time.time(),main())







    
