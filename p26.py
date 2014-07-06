# Find the value of d < 1000 for which 1/d
# contains the longest recurring cycle in its decimal fraction part.

'''
hm... I originally wanted to convert the floats for 1/d -> strings -> int arrays,
thinking then I could traverse these arrays to look for cycles...
but I'm only getting 15 digits of precision by default, and beyond that, I can't be
certain that how many digits of precision I actually need. All the inputs are rational,
so fractional part will contain some repetition, but can I find a bound on it?

Here's an interesting question that speaks to a larger principle:

Which fractions are most difficult to represent in base 10? In converting from one base
to another, where are we most likely to run into these unterminating representations?


'''

def main():
	return 0

def to_string(n):
	f = float(1)/n
	a = str(f).split('.')[1][:-1]
	print f, a

if __name__ == '__main__':
	import boilerplate, time
	boilerplate.all(time.time(),main())
