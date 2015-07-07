import matplotlib.pyplot as plt
import seaborn
import time, math, random


def run(z,minn,maxn,num_samples):

    # generate samples for tests (rather than the fixed set sizes below)
    desired_mean = (maxn-minn)/2
    lambd = 1.0/desired_mean
    l = []
    i = 0
    while i < num_samples:
        new_num = random.expovariate(lambd)
        new_num = int(new_num)
        if new_num <= maxn and new_num >= minn:
            l.append(new_num)
            i += 1   
    l.sort()

    times = []
    #set_sizes = [1,5,10,20,35,100,200,500]
    set_sizes = l

    for n in set_sizes:
        t0 = time.time()
        z(n)
        times.append(time.time() - t0)


    plt.yscale('log')
    plt.xscale('log')


    norm_times = [(i/times[0])+set_sizes[1] for i in times]

    x0 = [1 for i in set_sizes]
    x1 = [math.log(i) for i in set_sizes]
    x2 = [i for i in set_sizes]
    x3 = [i**2 for i in set_sizes]
    x4 = [i**3 for i in set_sizes]
    x5 = [2**i for i in set_sizes[0:5]]

    plt.plot(set_sizes,x0,ls='--',label='1')
    plt.plot(set_sizes,x1,ls='--',label='log(n)')
    plt.plot(set_sizes,x2,ls='--',label='n')
    plt.plot(set_sizes,x3,ls='--',label='n^2')
    plt.plot(set_sizes,x4,ls='--',label='n^3')
    #plt.plot(set_sizes[0:5],x5,ls='--',label='2^n')

    plt.plot(set_sizes[1:],norm_times[1:], marker='o', label='normalized run times')

    plt.ylabel('time')
    plt.xlabel('input size')

    #plt.gca().set_xlim(left=1)
    plt.gca().set_ylim(bottom=0.01)

    plt.legend()
    plt.show()


