
'''
Print out if the list can sum to target

Challenge: 
*For a list of numbers and a target number, return true if any two numbers add to the target number
*Given a list of numbers, return a set of 3 numbers that add to 0.
'''

# Embedded loops. - O(n)
def sum_target(target, num_list):
    ans = False
    for i in num_list:
        for j in num_list:
            if (i+j) == target:
                ans = True
    return ans

#Recursive solution.
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


#Test section.
num_list = [5,3,5,7,1,2,5,6]
target = 20
target2 = 8
target3 = 0

result = True
result2 = False

implementations = [sum_target, sum_target2]

for impl in implementations:
    print "f(%s) == []: %s" % (target, impl(target, num_list) == result2)
    print "f(%s) == [5,3] or [7,1]: %s" % (target2, impl(target2, num_list) == result)
    print "f(%s) == []: %s" % (target3, impl(target3, num_list) == result2)
