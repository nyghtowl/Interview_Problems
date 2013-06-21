'''
Generate factorial
'''

import math

# Recursive solution
def rec_fact(n):
    if n == 0:
        return 1
    else:
        return (n * rec_fact(n-1))

print 0, rec_fact(4)

#---

#Loop solution
def factorial(n):
    num = n
    while num > 1:
        num -= 1
        n *= num
    return n

print 1, factorial(3)

#---

#Loop solution
def factorial2(n):
    for num in range(1,n):
        n *= num
    return n

print 2, factorial2(3)

#---

#List comprehension solution
def factorial3(n):return reduce(lambda x,y:x*y,[1]+range(1,n+1))

print 3, factorial3(3)

#---

#math library solution
print 4, math.factorial(3)