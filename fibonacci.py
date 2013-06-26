'''
Fibonacci - each number equals the sum of the two preceding numbers.

Fn = Fn-1 + Fn-2

Given a number, provide the fibonacci result in the sequence starting with 0

Challenge: account for negative or fraction numbers 

'''

#assumes no negatives or fractions entered and starting at 0
def fibonacci(num):
    if num == 0:
        return 0
    if num <= 2:
        return 1
    else:
        return fibonacci(num-1) + fibonacci(num-2)  



#test 
implementations = [fibonacci]

for impl in implementations:
    print "trying %s" % impl
    print "  f(0) == 0: %s" % (impl(0) == 0)
    print "  f(1) == 1: %s" % (impl(1) == 1)
    print "  f(2) == 1: %s" % (impl(2) == 1)
    print "  f(3) == 2: %s" % (impl(3) == 2)
    print "  f(6) == 8: %s" % (impl(6) == 8)
    print "  f(13) == 233: %s" % (impl(13) == 233)

