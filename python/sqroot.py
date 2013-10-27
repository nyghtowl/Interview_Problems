# assume positive n
# Newton's method is a popular solution for square root, but not implemented here.

'''
Find the square root of n.
'''

def sqrt(n):
    for number in range(0, n):
        if isSqrt(number,n):
            return number
        else:
            if n < number * number:
                return number, number - 1

'''
Helper function to use in sqrt function to calculate number squared
'''
def isSqrt(a,b):
    if a * a == b:
        return True
    else:
        return False

print sqrt(30)


