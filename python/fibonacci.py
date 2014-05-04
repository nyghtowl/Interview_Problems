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

# O(2^n)
def fib_recursive(num):
    if num < 2:
        return num
    else:
        return fib_recursive(num - 1) + fib_recursive(num - 2)

def fib_generator(num):
    fib_1 = fib_2 = 0
    for n in range(num):
        if n == 0:
            fib_2 = 1
            yield fib_1
        elif n == 1:
            yield fib_2
        else:
            next = fib_1 + fib_2
            yield next
            fib_1 = fib_2
            fib_2 = next

# O(n)
def fib_iteration2(index):
    results = [0, 1]
    if index < 2:
        return index
    for i in range(1, index):
        new_val = results[0] + results[1]
        results[0], results[1] = results[1], new_val
    return results[-1]

# O(n) - how to get adjustment if 3 returns 1?
def fib_variation(n):
    a, b, c, d = 0, 1, 1, 1
    for i in range(n):
        a, b, c, d = b, c, d, c+d
    return sum(a, b, c, d)

if __name__ == '__main__':

    # Test section
    implementations = [fib_iteration, fib_iteration2, fib_recursive, fib_variation]

    for impl in implementations:
        print "trying %s" % impl
        print "  f(0) == 0: %s" % (impl(0) == 0)
        print "  f(1) == 1: %s" % (impl(1) == 1)
        print "  f(2) == 1: %s" % (impl(2) == 1)
        print "  f(3) == 2: %s" % (impl(3) == 2)
        print "  f(6) == 8: %s" % (impl(6) == 8)
        print "  f(13) == 233: %s" % (impl(13) == 233)

    # Special case trying out generator
    gen_example = fib_generator(13)
    print "trying generator"
    print "  f(0) == 0: %s" % (gen_example.next() == 0)
    print "  f(1) == 1: %s" % (gen_example.next() == 1)
    print "  f(2) == 1: %s" % (gen_example.next() == 1)
    print "  f(3) == 2: %s" % (gen_example.next() == 2)