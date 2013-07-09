
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
        for i in num_list[index+1:]:
            if (elem + i) == target:
                if [elem, i] not in pairs and [i, elem] not in pairs:
                    pairs.append([elem,i])
    return pairs

#Broken down into multiple functions. - O(n^2)
#Finds if the numbers sum to 0.
def sum_num(target, num_1, num_2):
    return (num_1 + num_2 == target)

#
def compare_val(target, val, num_list):
    for i in num_list:
        if sum_num(target,val,i):
                return [val, i]

def sum_target4(target, num_list):
    pairs = []
    for index, val in enumerate(num_list):
        if compare_val(target, val, num_list[index+1:]):
            a, b = compare_val(target, val, num_list[index+1:])
            if [a, b] not in pairs and [b, a] not in pairs:
                pairs.append(compare_val(target, val, num_list[index+1:]))
    return pairs

#O(n)
def sum_target5(target, num_list):
    pairs = {}

    # target - val in list
    for val in num_list:
        x = target - val
        if x in num_list and x not in pairs:
            pairs[val] = x
    return pairs

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
    print "trying %s" % impl
    print "f(%s) == []: %s" % (target, impl(target, num_list) == result2)
    print "f(%s) == [5,3] or [7,1]: %s" % (target2, impl(target2, num_list) == result)
    print "f(%s) == []: %s" % (target3, impl(target3, num_list) == result2)


#List of values results
result3 = []
result4 = [[5,3],[7,1],[2,6]]
result5 = []

implementations2 = [sum_target3, sum_target4]
for impl in implementations2:
    print "trying %s" % impl
    print "f(%s) == %s: %s" % (num_list, target, impl(target, num_list) == result3)
    print "f(%s) == %s: %s" % (num_list, target2, impl(target2, num_list) == result4)
    print "f(%s) == %s: %s" % (num_list, target3, impl(target3, num_list) == result5)


result6 = {2: 6, 5: 3, 7: 1}
implementations2 = [sum_target5]

for impl in implementations2:
    print "trying %s" % impl
    print "f(%s) == %s: %s" % (num_list, target2, impl(target2, num_list) == result6)
