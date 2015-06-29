def main(n): # num from 1 to 1000 in words = how many letters?
	d = {1:3, 2:3, 3:5, 4:4, 5:4, 6:3, 7:5, 8:5, 9:4, 10:3, 11:6, 12:6, 13:8, 14:8, 15:7,
		16:7, 17:7, 18:8, 19:8, 20:5, 30:6, 40:6, 50:5, 60:6, 70:7, 80:6, 90:6}
		# don't forget 'hundred' & 'and' (...that'll be in the conditional logic)

	total_count = 0
	for i in xrange(1,n+1):	
		if i in d:
			total_count += d[i] 
		elif (i<100):
			dig1 = (i/10)*10
			dig2 = i%10
			total_count += d[dig1] + d[dig2]
		elif (i>=100 and i<1000):
			print "do something a little bit more complex than the previous clause"
		elif (i == 1000):
			total_count += 11
		else:
			print "number range error: n must be in the range 1:1000"

	return total_count

if __name__ == '__main__':
	import boilerplate, time
	boilerplate.all(time.time(),main(99))