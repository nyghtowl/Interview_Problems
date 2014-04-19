'''
MCMC from Scratch

Algorithm for sampling probability distributions.
Approximates target distribution

Code from : http://darrenjw.wordpress.com/2010/04/28/mcmc-programming-in-r-python-java-and-c/

f(x,y) = k x2 exp{-xy2-y2+2y-4x}

'''

import random, math
 
def gibbs(N=20000,thin=500):
    x=0
    y=0
    print "Iter  x  y"
    for i in range(N):
        for j in range(thin):
            x=random.gammavariate(3,1.0/(y*y+4))
            y=random.gauss(1.0/(x+1),1.0/math.sqrt(x+1))
        print i,x,y
     
gibbs()