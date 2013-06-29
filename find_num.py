'''
Find a num in a list 
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


#Test for find number variations 
implementations = [find_num, find_num2]
list1 = [5,4,1,2,8,3,-1,3,1]

for impl in implementations:
    print "trying %s" % impl
    print "  f(list1, 0) == False or Doesn't exist: %s" % (impl(list1, 0) == False or impl(list1, 0) == "Doesn't exist")
    print "  f(list1, 1) == True or 8: %s" % (impl(list1, 1) == True or impl(list1, 1) == 8)
    print "  f(list1, 2) == True or Doesn't exist: %s" % (impl(list1, 2) == True or impl(list1, 2) == "Doesn't exist")
    print "  f(list1, 3) == True or 7: %s" % (impl(list1, 3) == True or impl(list1, 3) == 7)

