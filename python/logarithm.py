'''
Compute Logarithm

x: a positive integer
b: a positive integer; b >= 2

returns: log_b(x), or, the logarithm of x relative to a base b. 

Assumes: It should only return integer value and solution is recursive.
'''


def myLog(x, b):
    if x < b:
        return 0
    else:
        return myLog(x/b, b) + 1

if __name__ == '__main__':

    # Test section
    implementations = [myLog]

    for impl in implementations:
        print "trying %s" % impl
        print "  f(1, 2) == 0: %s" % (impl(1,2) == 0)
        print "  f(2, 2) == 1: %s" % (impl(2,2) == 1)
        print "  f(16, 2) == 4: %s" % (impl(16,2) == 4)
        print "  f(15, 3) == 2: %s" % (impl(15,3) == 2)
        print "  f(15, 4) == 1: %s" % (impl(15,4) == 1)
