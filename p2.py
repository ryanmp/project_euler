def main(l):
	new = l[-2] + l[-1]
	if new > 4e6:
		print sum(l[1:-1:2])
	else:
		l.append(new)	
		main(l)

if __name__ == '__main__':
	import boilerplate
	boilerplate.all(main())
