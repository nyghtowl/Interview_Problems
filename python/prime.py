'''
Find Prime Number

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

#Test section
impl = find_primes
sample_n = [1,6,7,100]
results = [[],[2,3],[7],[2,5]]
for index, n in enumerate(sample_n):
    # print "trying %s" % impl
    print "f(%s) == %s: %s" % (n,results[index],(impl(n) == results[index]))


# print "1: ",find_primes(1)
# print "6: ",find_primes(6)
# print "7: ",find_primes(7)
# print "100: ",find_primes(100)
