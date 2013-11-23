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

'''
Write a generator, genPrimes, that returns the sequence of prime numbers on successive calls to its next() method: 2, 3, 5, 7, 11, ...
'''

def genPrimes():
    primes = []   # primes generated so far
    last = 1      # last number tried
    while True:
        last += 1
        for p in primes:
            if last % p == 0:
                break
        else:
            primes.append(last)
            yield last

if __name__ == '__main__':
    #Test section
    impl = find_primes
    sample_n = [1,6,7,100]
    results = [[],[2,3],[7],[2,5]]
    print "trying find_primes"
    for index, n in enumerate(sample_n):
        # print "trying %s" % impl
        print "f(%s) == %s: %s" % (n,results[index],(impl(n) == results[index]))

    print "trying genPrimes"
    prime_print = genPrimes()
    print "first round == 2: %s" % (prime_print.next() == 2)
    print "first round == 3: %s" % (prime_print.next() == 3)
    print "first round == 5: %s" % (prime_print.next() == 5)
