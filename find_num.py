'''
Find a num in a list or a missing number between lists
'''

alist = [1, 2, 3, 4, 5, 6, 3]

#return true if num exists in list
def find_num(alist, num):
    if num in alist:
        return True

print 1, find_num(alist, 3)

#---

#return index of the second occurance of a num in list
def find_num2(alist, num):
    count = 0
    for x, n in enumerate(alist):
        if n == num:
            count += 1
            if count == 2:    
                return x
            else:
                print "Two occurances doesn't exist"

print 2, find_num2(alist, 3)

#---

list1 = [5,4,7,2,1,8,3]
list2 = [8,1,2,7,5,3]

#find a missing number when comparing two lists
def miss_num(list1, list2):
    
    for i in list1:
        if i not in list2:
            return i

print miss_num(list1, list2)

#---

#second variation to find a missing number by adding the values and subtracting
def miss_num2(list1, list2):
    return abs(sum(list1)-sum(list2))

print miss_num2(list1, list2)
