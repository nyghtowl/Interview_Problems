'''
Prime - 4th Clean Chain

Input: Take a sequence of N numbers. We'll call the sequence a "Clean Chain of length N" if the sum of the first N - 1 numbers is evenly divisibly by the Nth number.

For example, the sequence [2, 4, 6, 8, 10] forms a clean chain of length 5, since 2 + 4 + 6 + 8 = 20, which is divisible by 10, and the sequence has 5 numbers.
The first clean chain formed out of the sequence of primes is simply [2], with length 1.
The second is [2, 3, 5] with length 3.
The third is [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71], with length 20

Output: What is the length of the fourth clean chain formed out of only primes?

Bonus: major bonus points, find the length of the fifth chain, too, and include it in the comments.

Contribution: Jess

'''

'''
Answer: Nathan Lucas (https://github.com/bnlucas)

The code below was taken from my reversible obfuscated hashing library, BaseHash
(https://github.com/bnlucas/python-basehash) found under basehash/primes.py

More information on the work behind the verification of primes can be found at
http://coderwall.com/p/utwriw and http://coderwall.com/p/t0u70w discussing the
process of developing these methods.

[     2,      3,      5,      7,     11,     13,     17,     19,     23,     29,
     31,     37,     41,     43,     47,     53,     59,     61,     67,     71,
    ...,
 368911, 368939, 368947, 368957, 369007, 369013, 369023, 369029, 369067, 369071,
 369077, 369079, 369097, 369119]

For the full fourth chain, all 3147 lines, see https://gist.github.com/bnlucas/7803398
There is a verifier at the bottom of the gist to ensure it is not skipping anything.

 prime       prev. sum       remainder
     2               0               0    1st clean chain
     5               5               0    2nd clean chain
    71             568               0    3rd clean chain
369119      5536785000               0    4th clean chain
'''

from fractions import gcd


PRIMES_LE_31 = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31)
PRIMONIAL_31 = 200560490130


def isqrt(n):
    if n < 0:
        raise ValueError('Square root is not defined for negative numbers.')
    x = int(n)
    if x == 0:
        return 0
    a, b = divmod(x.bit_length(), 2)
    n = 2 ** (a + b)
    while True:
        y = (n + x // n) >> 1
        if y >= n:
            return n
        n = y


def is_square(n):
    s = isqrt(n)
    return s * s == n


def factor(n, p=2):
    s = 0
    d = n - 1
    q = p

    while not d & q - 1:
        s += 1
        q *= p

    return s, d // (q // p)


def jacobi(a, p):
    if (not p & 1) or (p < 0):
        raise ValueError('p must be a positive odd number.')

    if (a == 0) or (a == 1):
        return a

    a = a % p
    t = 1

    while a != 0:
        while not a & 1:
            a >>= 1
            if p & 7 in (3, 5):
                t = -t

        a, p = p, a
        if (a & 3 == 3) and (p & 3) == 3:
            t = -t

        a = a % p

    if p == 1:
        return t

    return 0


def selfridge(n):
    d = 5
    s = 1
    ds = d * s

    while True:
        if gcd(ds, n) > 1:
            return ds, 0, 0

        if jacobi(ds, n) == -1:
            return ds, 1, (1 - ds) / 4

        d += 2
        s *= -1
        ds = d * s


def chain(n, u1, v1, u2, v2, d, q, m):
    k = q
    while m > 0:
        u2 = (u2 * v2) % n
        v2 = (v2 * v2 - 2 * q) % n
        q = (q * q) % n

        if m & 1 == 1:
            t1, t2 = u2 * v1, u1 * v2
            t3, t4 = v2 * v1, u2 * u1 * d
            u1, v1 = t1 + t2, t3 + t4

            if u1 & 1 == 1:
                u1 = u1 + n

            if v1 & 1 == 1:
                v1 = v1 + n

            u1, v1 = (u1 / 2) % n, (v1 / 2) % n
            k = (q * k) % n

        m = m >> 1

    return u1, v1, k


def strong_pseudoprime(n, a, s=None, d=None):
    if not n & 1:
        return False

    if (s is None) or (d is None):
        s, d = factor(n, 2)

    x = pow(a, d, n)

    if x == 1:
        return True

    for i in xrange(s):
        if x == n - 1:
            return True

        x = pow(x, 2, n)

    return False


def lucas_pseudoprime(n):
    if not n & 1:
        return False

    d, p, q = selfridge(n)
    if p == 0:
        return n == d

    u, v, k = chain(n, 0, 2, 1, p, d, q, (n + 1) >> 1)
    return u == 0


def strong_lucas_pseudoprime(n):
    if not n & 1:
        return False

    d, p, q = selfridge(n)
    if p == 0:
        return n == d

    s, t = factor(n + 2)

    u, v, k = chain(n, 1, p, 1, p, d, q, t >> 1)

    if (u == 0) or (v == 0):
        return True

    for i in xrange(1, s):
        v = (v * v - 2 * k) % n
        k = (k * k) % n
        if v == 0:
            return True

    return False


def baillie_psw(n, limit=100):
    if n == 2:
        return True

    if not n & 1:
        return False

    if n < 2 or is_square(n):
        return False

    if gcd(n, PRIMONIAL_31) > 1:
        return n in PRIMES_LE_31

    bound = min(limit, isqrt(n))
    for i in xrange(3, bound, 2):
        if not n % i:
            return False

    return strong_pseudoprime(n, 2) \
        and strong_pseudoprime(n, 3) \
        and strong_lucas_pseudoprime(n)


def next_prime(n):
    if n < 2:
        return 2

    if n < 5:
        return [3, 5, 5][n - 2]

    gap = [1, 6, 5, 4, 3, 2, 1, 4, 3, 2, 1, 2, 1, 4, 3, 2, 1, 2, 1, 4, 3, 2, 1,
           6, 5, 4, 3, 2, 1, 2]

    n += 1 if not n & 1 else 2

    while not baillie_psw(n):
        n += gap[n % 30]

    return n


def is_clean_prime_chain(prime):
    return sum(prime[:-1]) % prime[-1] == 0


def clean_prime_chain(prime):
    while True:
        prime.append(next_prime(prime[-1]))

        if is_clean_prime_chain(prime):
            return prime
