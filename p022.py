def main(): 
	names = open('p022.in').read().split(',') #file -> list
	names = [i[1:-1] for i in names] # stripping extra quotes
	names.sort()
	total_score = 0
	for idx, name in enumerate(names, start=1):
		name_score = 0
		for n in list(name): # score each letter
			name_score += ord(n.lower())-96 # char -> int
		name_score *= idx
		total_score += name_score
	return total_score

if __name__ == '__main__':
	import boilerplate, time, resource
	t = time.time()
	r = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
	boilerplate.all(main(), t, r)


	