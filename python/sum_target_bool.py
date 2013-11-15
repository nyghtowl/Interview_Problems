'''
Sum Target / Combination Validation

n is an int

Returns True if some integer combination of 6, 9 and 20 equals n
Otherwise returns False.

'''
from __future__ import division # brings in math from python 3.0
import time

# O(n^3)
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

# O(1) - because combo sizes are fixed
def target_combo2(n):
    combo_sizes = [20, 9, 6]
    remaining = n
    for combo_size in combo_sizes:
        remaining -= (remaining // combo_size) * combo_size
    return remaining == 0

def do_thing(thing, *args):
    start = time.time()
    thing(*args)
    return time.time() - start

if __name__ == '__main__':

    # Test section
    implementations = [target_combo, target_combo2]

    for impl in implementations:
        print "trying %s" % impl
        print "  f(6) is %s" % (impl(6)==True)
        print "  f(7) is %s" % (impl(7)==False)
        print "  f(100000000) is %s seconds" % (do_thing(impl, 100000000))
