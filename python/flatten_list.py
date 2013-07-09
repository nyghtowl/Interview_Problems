'''
Flatten Lists

Input: multiple Lists
Output: contcatenation of lists into one
'''

def flatten_list(l):
    return [item for sublist in l for item in sublist]


#Test
l = [[1,2],[3,4],[5,6]]
result = [1,2,3,4,5,6]

implementations = [flatten_list]

for impl in implementations:
    print "trying %s" % impl
    print "  f(l) == %s: %s" % (result, (impl(l) == result))

