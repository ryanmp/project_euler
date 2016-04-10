# needs to also pickle some sort of python list/array, to add each new
# time data point

import time
import resource

def all(x, t = None, m = None):
	
	ret = x
	print "answer:", ret

	if t is not None:
		start_time = t
		run_time = time.time() - start_time
		print "time:", run_time

	if m is not None:
		start_mem = m
		print "mem usage:", resource.getrusage(resource.RUSAGE_SELF).ru_maxrss - start_mem
