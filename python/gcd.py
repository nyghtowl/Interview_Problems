#!/usr/bin/env python
''' 
Greatest Common Divisor

Input: Two positive integers
Output: Largest integer that divides into both

Sample problem from edx CompSci 101

'''
def gcd(a, b):
    test_value = min(a, b)
    if a % test_value == 0 and b % test_value == 0:
        return test_value
    while test_value > 0:
        test_value -= 1
        if a % test_value == 0 and b % test_value == 0:
            return test_value

def gcd2(a, b):
    testValue = min(a, b)

    # Keep looping until testValue divides both a & b evenly
    while a % testValue != 0 or b % testValue != 0:
        testValue -= 1


if __name__ == '__main__':
    # Test section
    implementations = [gcd, gcd2]

    for impl in implementations:
        print "trying %s" % impl
        print "  f(2,12) == 2: %s" % (gcd(2,12) == 2)
        print "  f(6,12) == 6: %s" % (gcd(6,12) == 6)
        print "  f(17,12) == 1: %s" % (gcd(17,12) == 1)
