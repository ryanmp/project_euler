# needs to also pickle some sort of python list/array, to add each new
# time data point

import time

def all(x):
	start_time = time.time()
	ret = x
	print "answer:", ret
	run_time = time.time() - start_time
	print "time:", run_time
