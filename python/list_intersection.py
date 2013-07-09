'''
List Intersection

Input: 2 lists
Output: points of intersection between 2 lists
'''

#Return list of intersections between 2 lists - O(n^2) or O(nm)
def list_int(list1, list2):
    result = []
    for a in list1:
        for b in list2:
            if a == b:
                result.append(a)
    return set(result)

#Return list of intersections between 2 lists - O(n^2) or O(nm)
def list_int2(list1, list2):
    result = []
    for a in list1: 
        if a in list2: #'in' is a loop
            result.append(a)
    return set(result)

#Return list of intersections using list and set functions - O(n)
def list_int3(list1, list2):
    return set(list(set(list1) & set(list2)))

#Create a dictionary and then run through to build list with list comprehension - O(n)
def list_int4(list1, list2):
    s1 = set(list1)
    lc = [list2[i] for i in xrange(len(list2)) if list2[i] in s1]
    return set(list(lc))

#Test for find number variations 
implementations = [list_int, list_int2, list_int3, list_int4]
list1 = [9,-1,10,2,300,3,0,-10]
list2 = [5,4,7,-1,8,9]
list3 = [-2,0,2000,30,16,85,903,-10,567,4,300]
list4 = [-2,2000,30,16,85,903,567,4]

for impl in implementations:
    print "trying %s" % impl
    print "  f(list1, list2) == [9,-1]: %s" % (impl(list1, list2) == set([9,-1]))
    print "  f(list1, list3) == [0,-10,300]: %s" % (impl(list1, list3) == set([0,-10,300]))
    print "  f(list2, list3) == [4]: %s" % (impl(list2, list3) == set([4]))
    print "  f(list1, list4) == []: %s" % (impl(list1, list4) == set([]))
    print impl(list1, list3)

