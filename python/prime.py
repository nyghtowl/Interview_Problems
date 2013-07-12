'''
Find Prime Number
'''

# Function to find the set of prime divisors of a number
# Assumes that the number given is a positive integer
#
def find_primes(n):
    possible_divisor = 2
    primes = set()
    while n != 1:
        while n % possible_divisor == 0:
            primes.add(possible_divisor)
            n /= possible_divisor
        possible_divisor += 1
    return primes

print "1: ",find_primes(1)
print "7: ",find_primes(7)
print "100: ",find_primes(100)
