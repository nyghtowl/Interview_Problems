'''
Find the square root of n.

    Input: A number
    Output: The square root or the integers closest to the square root
    Assume: positive n

 Newton's method is a popular solution for square root, but not implemented here.
'''

def sqrt(n):
    for number in range(0, n):
        if isSqrt(number,n):
            return number
        else:
            if n < number * number:
                return number, number - 1


def isSqrt(a,b):
    '''
    Helper function to use in sqrt function to calculate number squared
    '''
    if a * a == b:
        return True
    else:
        return False


# Test Section
if __name__ == '__main__':
    print "sqrt(25) = 5: %s" % (sqrt(25) == 5)
    print "sqrt(30) = (6, 5): %s" % (sqrt(30) == (6,5))

