#!/usr/bin/env python
'''
Prime Number

Input: positive integer
Output: set of prime divsors of a number

'''

def find_primes(n):
    possible_divisor = 2
    primes = set()
    while n != 1:
        while n % possible_divisor == 0:
            primes.add(possible_divisor)
            n /= possible_divisor
        possible_divisor += 1
    return list(primes)

if __name__ == '__main__':
    #Test section
    impl = find_primes
    sample_n = [1,6,7,100]
    results = [[],[2,3],[7],[2,5]]
    for index, n in enumerate(sample_n):
        # print "trying %s" % impl
        print "f(%s) == %s: %s" % (n,results[index],(impl(n) == results[index]))


