'''
The nth term of the sequence of triangle numbers is given by, tn = (1/2)n(n+1); so the first ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its alphabetical position
and adding these values we form a word value. For example, the word value for SKY is 19 + 11 + 25 = 55 = t10.
If the word value is a triangle number then we shall call the word a triangle word.

Using the included 16K text file containing nearly two-thousand common English words, how many are triangle words?

'''


def main(): 
	lines = open('p042.in').read().split(',')

	arr = []
	for line in lines:
		line = line.replace('"', '').strip()
		arr.append(sum([ord(i)-64 for i in line]))

	test_set = tri_numbers_below_n(max(arr))

	count = 0
	for word_sum in arr:
		for tri in test_set:
			if word_sum == tri:
				count += 1

	return count


def tri_number(n):
	return int((1.0/2.0)*n*(n+1))


def tri_numbers_below_n(n):
	tris = []
	result = 0
	i = 1
	while result <= n:
		result = tri_number(i)
		tris.append(result)
		i += 1
	return tris


if __name__ == '__main__':
	import boilerplate, time
	boilerplate.all(time.time(),main())

