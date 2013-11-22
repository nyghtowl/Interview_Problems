#!/usr/bin/env python
'''
Fibonacci - each number equals the sum of the two preceding numbers.

Fn = Fn-1 + Fn-2

Input: the point in the sequence to take a fibonnaci number
Output: the fibonnaci number at the point in a sequence starting a 0

Ex: 
At position 0 the Fib number is 0. 
At position 4 the Fib number is 3 (adding 1, 2 which are the numbers before)

Challenge:
* Account for negative or fraction numbers
* Do it more efficiently (memoization)?
* Do it with only O(1) space (iteratively using a for loop)

'''

# O(n)


def fib_iteration(num):
    alist = []
    first = 0
    second = 1
    while num >= 0:
        alist.append(first)
        num -= 1
        first, second = second, (first + second)
    return alist[num]


def fib_recursive(num):
    if num == 0:
        return 0
    if num <= 2:
        return 1
    else:
        return fib_recursive(num - 1) + fib_recursive(num - 2)

def fib_generator(num):
    fib_1 = 0
    fib_2 = 1
    for n in range(num):
        next = fib_1 + fib_2
        yield next
        fib_1 = fib_2
        fib_2 = next

if __name__ == '__main__':

    # Test section
    implementations = [fib_iteration, fib_recursive]

    for impl in implementations:
        print "trying %s" % impl
        print "  f(0) == 0: %s" % (impl(0) == 0)
        print "  f(1) == 1: %s" % (impl(1) == 1)
        print "  f(2) == 1: %s" % (impl(2) == 1)
        print "  f(3) == 2: %s" % (impl(3) == 2)
        print "  f(6) == 8: %s" % (impl(6) == 8)
        print "  f(13) == 233: %s" % (impl(13) == 233)

    # Special case trying out generator
    print fib_generator(13)
