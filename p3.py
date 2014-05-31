import time
def main(n):
	current_sum = n
	prime_factors = []
	for i in range(2,n):
		if current_sum%i == 0:
			current_sum = current_sum/i
			prime_factors.append(i)
	return prime_factors[-1]
if __name__ == '__main__':
	
	start_time = time.time()
	#print main(600851475143)
	print main(1234)
	print time.time() - start_time
