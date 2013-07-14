#!/usr/bin/env python
'''
Flatten Lists

Input: multiple Lists
Output: contcatenation of lists into one
'''

#List comprehension - O(n)
def flatten_list(list_of_lists):
    return [item for sublist in list_of_lists for item in sublist]


#Test section
list_of_lists = [[1,2],[3,4],[5,6]]
result = [1,2,3,4,5,6]

implementations = [flatten_list]

for impl in implementations:
    print "trying %s" % impl
    print "  f(%s) == %s: %s" % (list_of_lists, result, (impl(l) == result))

