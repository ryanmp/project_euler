def main():
	l = [1,2]
	return inner(l)

def inner(l):
	new = l[-2] + l[-1]
	if new > 4e6:
		return sum(l[1:-1:2])
	else:
		l.append(new)	
		inner(l)

if __name__ == '__main__':
	import boilerplate, time
	boilerplate.all(time.time(),main())
