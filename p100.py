'''

If a box contains twenty-one coloured discs, composed of fifteen blue discs and six red discs,
and two discs were taken at random, it can be seen that the probability of taking two blue discs,
P(BB) = (15/21)*(14/20) = 1/2.

The next such arrangement, for which there is exactly 50 percent chance of taking two blue discs
at random, is a box containing eighty-five blue discs and thirty-five red discs.

By finding the first arrangement to contain over 10^12 = 1,000,000,000,000 discs in total,
determine the number of blue discs that the box would contain.

solution:

(b/(b+r))*((b-1)/(b+r-1)) = 1/2, b & r are Integers > 0
coded integer solution (found equations via wolfram alpha)


'''

from math import sqrt

c1 = 3 - 2*sqrt(2)
c2 = 3 + 2*sqrt(2)

def b(n):
	sol = 0
	sol += 2*c1**n
	sol += sqrt(2)*c1**n
	sol += 2*c2**n
	sol += sqrt(2)*c2**n
	sol += 4
	sol *= (1.0/8.0)
	return int(round(sol))

def r(n):
	n = n+1
	sol = 0
	sol += -4*c1**n
	sol += -3*sqrt(2)*c1**n
	sol += -4*c2**n
	sol += 3*sqrt(2)*c2**n
	sol *= (1.0/8.0)
	return int(round(sol))

def main():
	i = 2
	while True:
		i += 1
		if r(i) + b(i) > 1e12:
			return b(i)

if __name__ == '__main__':
	import boilerplate, time
	boilerplate.all(time.time(),main())









