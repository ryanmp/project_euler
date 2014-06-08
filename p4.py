def main():
	i = 999
	j = 999
	while(True):
		if is_palindrome(i*j):
			return i*j
		i -= 1
		if is_palindrome(i*j):
			return i*j
		j -= 1

def is_palindrome(n):
	return str(n) == str(n)[::-1]

if __name__ == '__main__':
	import boilerplate
	boilerplate.all(main())
