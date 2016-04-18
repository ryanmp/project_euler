import re, os
def run_all():
	all_files = [f for f in os.listdir('.') if os.path.isfile(f)]
	all_problems = []
	for i in all_files:
		m = re.match("^p.*\d.py", i)
		if m:
			all_problems.append(i)

	all_problems = all_problems[0:12] # just do a couple for testing purposes

	# runs every solution script in this directory
	for i in all_problems:
		print '------------------------------'
		print 'executing: ' + i
		execfile(i, globals())
		print 'lines of code: ' + str(num_lines(i)[0])

# prints the number of lines in every p###.py file in this dir
def all_lines(files):
	for i in files:
		print num_lines(i)

# this will analyze number of lines of all p_ and relative running times
def num_lines(fname):

	lines_with_code = 0
	lines_with_comments = 0
	inside_comment = False

	with open(fname) as f:
		for i, l in enumerate(f):
			if inside_comment:
				lines_with_comments += 1
			if '\'\'\'' in l:
				inside_comment = not inside_comment
				lines_with_comments += 1
			elif '#' in l:
				lines_with_comments += 1

			elif inside_comment == False and len(l) > 1:
				lines_with_code += 1

			pass
	return lines_with_code - 5, lines_with_comments # remove 5 for our call to boilerplate

if __name__ == '__main__':
	run_all()
