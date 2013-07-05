'''
Find a missing number between lists or find intersection points
'''

#Find a missing number when comparing two lists.
def miss_num(list1, list2):
    
    for i in list1:
        if i not in list2:
            return i
    return 0


#Second variation to find a missing number by adding the values and subtracting.
def miss_num2(list1, list2):
    return abs(sum(list1)-sum(list2))


#Test for find number variations 
implementations = [miss_num, miss_num2]
list1 = [5,4,7,2,1,8,3]
list2 = [5,4,7,2,8,3]
list3 = [5,4,7,2,1,8,3]

for impl in implementations:
    print "trying %s" % impl
    print "  f(list1, list2) == 1: %s" % (impl(list1, list2) == 1)
    print "  f(list1, list3) == 0: %s" % (impl(list1, list3) == 0)
