''' 
Square a number
'''

#Simple solution
def square(num):
    return num * num

#Loop / list comprehension solution.
def square2(num):
    return sum([num for n in range(num)])

#Test cases
implementations = [square, square2]

for impl in implementations:
    print "trying %s" % impl
    print "  f(0) == 0: %s" % (impl(0) == 0)
    print "  f(1) == 1: %s" % (impl(1) == 1)
    print "  f(2) == 4: %s" % (impl(2) == 4)
    print "  f(3) == 9: %s" % (impl(3) == 9)
    print "  f(10) == 100: %s" % (impl(10) == 100)
