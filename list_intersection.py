'''
Find list intersection
'''

#Return list of intersections between 2 lists - O(n^2) or O(nm)
def list_intersection(list1, list2):
    result = []
    for a in list1:
        for b in list2:
            if a == b:
                result.append(a)
    return result

#Return list of intersections between 2 lists - O(n^2) or O(nm)
def list_intersection2(list1, list2):
    result = []
    for a in list1: 
        if a in list2: #'in' is a loop
            result.append(a)
    return result

#Return list of intersections using list and set functions - O(n)
def list_intersection3(list1, list2):
    return list(set(list1) & set(list2))

#O(n)
def list_intersection4(list1, list2):
    s1 = set(list1)
    lc = [list2[i] for i in xrange(len(list2)) if list2[i] in s1]
    return list(lc)

#Test for find number variations 
implementations = [list_intersection, list_intersection2, list_intersection3]
list1 = [9,-1,10,2,300,3]
list2 = [5,4,7,-1,8,9]

for impl in implementations:
    print "trying %s" % impl
    print "  f(list1, list2) == [9,-1]: %s" % (impl(list1, list2) == [9,-1])

