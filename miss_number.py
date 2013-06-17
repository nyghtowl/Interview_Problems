'''
Find a missing number
'''


list1 = [5,4,7,2,1,8,3]
list2 = [8,1,2,7,5,3]

def miss_num(list1, list2):
    
    for i in list1:
        if i not in list2:
            return i

print miss_num(list1, list2)

def miss_num2(list1, list2):
    return abs(sum(list1)-sum(list2))

print miss_num2(list1, list2)