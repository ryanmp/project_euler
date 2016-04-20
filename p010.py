'''

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.

'''

def main(): #returns sum of primes (ex n->2,000,000 = ???)
    n = 2000000
    return sum(primes(n))

def primes(n):
     # http://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188
    """ Returns  a list of primes < n """
    sieve = [True] * n
    for i in xrange(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)/(2*i)+1)
    return [2] + [i for i in xrange(3,n,2) if sieve[i]]

if __name__ == '__main__':
    import boilerplate, time, resource
    t = time.time()
    r = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    boilerplate.all(main(), t, r)
