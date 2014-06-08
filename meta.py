# this will
# analyze number of lines of all p_ and relative running times

def num_lines(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1 - (4) #4 for our boilerplate

# prints the number of lines in every p13434.py file in this dir
import re, os
files = [f for f in os.listdir('.') if os.path.isfile(f)]
for i in files:
	m = re.match("^p.*\d[.py]", i)
	if m:
		print num_lines(i)
