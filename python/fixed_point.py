"""
Fixed Point 

f: a function of one argument that returns a float
epsilon: a small float

returns the best guess when that guess is less than epsilon 
away from f(guess) or after 100 trials, whichever comes first.
"""

def fixedPoint(f, epsilon):
    guess = 1.0
    for i in range(100):
        if abs(f(guess) - guess) < epsilon:
            return guess
        else:
            guess = f(guess)
    return guess

def sqrt1(a):
    def tryit(x):
        return 0.5 * (a/x + x)
    return fixedPoint(tryit, 0.0001)

#################

def babylon(a):
    def test(x):
        return 0.5 * ((a / x) + x)
    return test

def sqrt2(a):
    return fixedPoint(babylon(a), 0.0001)


if __name__ == '__main__':

    # Test section
    implementations = [sqrt1, sqrt2]

    for impl in implementations:
        print "trying %s" % impl
        print "  f(25) == 5: %s" % (round(impl(25)) == 5)
        print "  f(5) == 2: %s" % (round(impl(5)) == 2)
        print "  f(4) == 2: %s" % (round(impl(4)) == 2)
