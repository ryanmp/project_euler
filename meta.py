import re, os
def run_all():
	all_files = [f for f in os.listdir('.') if os.path.isfile(f)]
	all_problems = []
	for i in all_files:
		m = re.match("^p.*\d.py", i)
		if m:
			all_problems.append(i)

	all_problems = all_problems[0:4] # just do a couple for testing purposes

	# runs every solution script in this directory
	for i in all_problems:
		print i
		execfile(i, globals())

# prints the number of lines in every p###.py file in this dir
def all_lines(files):
	for i in files:
		print num_lines(i)

# this will analyze number of lines of all p_ and relative running times
def num_lines(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1 - (4) #4 for our boilerplate

if __name__ == '__main__':
	run_all()
