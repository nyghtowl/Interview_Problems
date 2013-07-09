
'''
Sum Target

Input: List of numbers & target number 
Output: Each pair of numbers that adds up to target

Challenge: 
*For a list of numbers and a target number, return true if any two numbers add to the target number
*Given a list of numbers, return a set of 3 numbers that add to 0.
'''
#Functions provide true/false results

# Embedded loops. - O(n^2)
def sum_target(target, num_list):
    ans = False
    for i in num_list:
        for j in num_list:
            if (i+j) == target:
                ans = True
    return ans

#Recursive solution. - O(n)
def sum_target2(target, num_list):
    if len(num_list) <= 1 and num_list[0] != target:
        return False
    elif num_list[-2]:
        if (num_list[-2]+num_list[-1]) == target:
            return True
        else:
            return sum_target2(target, num_list[:-1])
    else:
        return False


#Functions provide lists answers

#O(n^2)
def sum_target3(target, num_list):
    pairs = []
    for index, elem in enumerate(num_list):
        # for i in range(len(ex[index+1:])):
        for i in num_list[index+1:]:
            if (elem + i) == 0:
                pairs.append((elem, i))
    return pairs

#Broken down into multiple functions - O(n^2)
def sum_num(num_1, num_2):
    return (num_1 + num_2 == 0)

def compare_val(num, num_list):
    for i in num_list:
        if sum_num(target,i):
    return (target, i)

def sum_target4(target, num_list):
    pairs = []
    for index, val in enumerate(num_list):
        pairs.append(compare_val(val, l[index+1:]))
    return pairs


'''
recusive example - question on whether this works
'''
# pairs = []
# l = [0,-1,5,3,1]

# def sum_recursive(l):
#     if len(l) < 2:
#         return 

#     elif (len(l) == 2) and (l[0] + l[1] == 0):
#         return (l[0],l[1])

#     else:

#         return (l[0] + sum_recursive(l[1:]) == 0)
 

# len(l) = 5
# l[0] = 0
# l[1] = -1
# l[1:] = [-1, 5, 3, 1]
# l[0] + sum_recursive = ?

# len(l) = 4


# target = 0

# pick and hold 1 element and loop through the rest of the list and add to compare if works



#Test section.
num_list = [5,3,5,7,1,2,5,6]
num_list2 = [0,-1,5,0,3,1]
target = 20
target2 = 8
target3 = 0

#True/false results
result = True
result2 = False

implementations = [sum_target, sum_target2]

for impl in implementations:
    print "f(%s) == []: %s" % (target, impl(target, num_list) == result2)
    print "f(%s) == [5,3] or [7,1]: %s" % (target2, impl(target2, num_list) == result)
    print "f(%s) == []: %s" % (target3, impl(target3, num_list) == result2)


#List of values results
result3 = []
result4 = [3,5,7,1]
result5 = []

implementations2 = [sum_target3, sum_target4]
for impl in implementations2:
    print "f(%s) == %s: %s" % (target, impl(target, num_list) == result3)
    print "f(%s) == %s: %s" % (target2, impl(target2, num_list) == result4)
    print "f(%s) == %s: %s" % (target2, impl(target2, num_list) == result5)
