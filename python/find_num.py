#!/usr/bin/env python
'''
Find Num 

Input: List of integers and target number.
Output: If the number exists and the index of the number  OR
What number is missing

'''

#Return true if num exists in list -O(n)
def find_num(list1, num):
    if num in list1:
        return True
    return False


#Return index of the second occurance of a num in list - O(n)
def find_num2(list1, num):
    count = result = 0
    for x, n in enumerate(list1):
        if n == num:
            count += 1
            if count == 2:    
                result = x
            else:
                result = "Doesn't exist"
    return result


#Find a missing number when comparing two lists - O(n^2)
def miss_num(list1, list2):
    
    for i in list1:
        if i not in list2:
            return i
    return 0


#Second variation to find a missing number by adding the values and subtracting - O(n)
def miss_num2(list1, list2):
    return abs(sum(list1)-sum(list2))


#Test section
implementations = [find_num, find_num2]
list1 = [5,4,1,2,8,3,-1,3,1]

result1 = True
result2 = False
result3 = "Doesn't exist"

for impl in implementations:
    print "trying %s" % impl
    print "  f(%s, 0) == False or Doesn't exist: %s" % (list1, (impl(list1, 0) == result2 or impl(list1, 0) == result3))
    print "  f(%s, 1) == True or 8: %s" % (impl(list1, 1) == (list1, result1 or impl(list1, 1) == 8))
    print "  f(%s, 2) == True or Doesn't exist: %s" % (list1, (impl(list1, 2) == True or impl(list1, 2) == result3))
    print "  f(%s, 3) == True or 7: %s" % (list1, (impl(list1, 3) == result1 or impl(list1, 3) == 7))

#Test for find miss number variations 
implementations2 = [miss_num, miss_num2]
list2 = [5,4,7,2,1,8,3]
list3 = [5,4,7,2,8,3]
list4 = [5,4,7,2,1,8,3]

for impl in implementations2:
    print "trying %s" % impl
    print "  f(%s, %s) == 1: %s" % (list2, list3, (impl(list2, list3) == 1))
    print "  f(%s, %s) == 0: %s" % (list3, list4, (impl(list3, list4) == 0))
