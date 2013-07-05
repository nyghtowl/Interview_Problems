'''
Find prime number
'''

# def find_prime(n):
#     list_p = []
#     for i in range(n):
#         if i == 0 or i == 1:
#             pass
#         elif (n % i) == 0:
#             if i != 2:
#                 if i % 2 == 0:
#                     pass
#             else:
#                 list_p += [i, ]
#     return list_p

# def prime_len(n):
#      prime_list = find_prime(n)
#      if len(prime_list) == len(n):
#           return prime_list
#      if len(prime_list) > len(n):
#           prime_list.pop()
#           prime_len(prime_list)
#      if len(prime_list) < len(n):
#           prime_len(prime_list.append(prime_list[1])

# print 7, prime_len(7)


# find the prime numbers that make up a submitted number
def find_prime2(n):
    plist = []
    n = abs(int(n))
    if n < 2:
        return "no primes"
    if n > 2:
        plist += [2,]
        for x in range(3, int(n**.5)+1, 2):
            if n % x == 0:
                pass
            else:
                plist.append(x)

    return plist

print find_prime2(100)
