
from fractions import gcd

def get_e(phi):
	for e in xrange(2,phi):
		if gcd(e,phi) == 1:
			return e
	return -1



p = 19
q = 37

n = p*q
phi = (p-1)*(q-1)

e = get_e(phi)

# in [0,n-1]
message = 123

def encrypt(m,e,n):
	return (m**e)%n



def decrypt(c,d,n):
	return (c**d)%n




