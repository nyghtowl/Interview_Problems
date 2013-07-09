'''
Find Num 

Input: List of integers and target number.
Output: If the number exists and the index of the number  OR
What number is missing

'''

#Return true if num exists in list.
def find_num(list1, num):
    if num in list1:
        return True
    return False


#Return index of the second occurance of a num in list.
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
implementations = [find_num, find_num2]
list1 = [5,4,1,2,8,3,-1,3,1]

result1 = True
result2 = False
result3 = "Doesn't exist"

for impl in implementations:
    print "trying %s" % impl
    print "  f(list1, 0) == False or Doesn't exist: %s" % (impl(list1, 0) == result2 or impl(list1, 0) == result3)
    print "  f(list1, 1) == True or 8: %s" % (impl(list1, 1) == result1 or impl(list1, 1) == 8)
    print "  f(list1, 2) == True or Doesn't exist: %s" % (impl(list1, 2) == True or impl(list1, 2) == result3)
    print "  f(list1, 3) == True or 7: %s" % (impl(list1, 3) == result1 or impl(list1, 3) == 7)

#Test for find miss number variations 
implementations2 = [miss_num, miss_num2]
list1 = [5,4,7,2,1,8,3]
list2 = [5,4,7,2,8,3]
list3 = [5,4,7,2,1,8,3]

for impl in implementations2:
    print "trying %s" % impl
    print "  f(list1, list2) == 1: %s" % (impl(list1, list2) == 1)
    print "  f(list1, list3) == 0: %s" % (impl(list1, list3) == 0)
