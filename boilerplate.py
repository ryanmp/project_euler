# needs to also pickle some sort of python list/array, to add each new
# time data point

import time

def all(t, x):
	start_time = t
	ret = x
	print "answer:", ret
	run_time = time.time() - start_time
	print "time:", run_time