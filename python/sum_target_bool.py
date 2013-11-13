'''
Sum Target / Combination Validation

n is an int

Returns True if some integer combination of 6, 9 and 20 equals n
Otherwise returns False.

'''


def target_combo(n):
    a = b = c = 0
    while (6 * a) <= n:
        while (9 * b) <= n:
            while (20 * c) <= n:
                ans = (6 * a) + (9 * b) + (20 * c)
                if ans == n:
                    return True
                c += 1
            c = 0
            b += 1
        c = b = 0
        a += 1

    return False


if __name__ == '__main__':

    # Test section
    implementations = [target_combo]

    for impl in implementations:
        print "trying %s" % impl
        print "  f(6) is %s" % (impl(6)==True)
        print "  f(7) is %s" % (impl(7)==False)
