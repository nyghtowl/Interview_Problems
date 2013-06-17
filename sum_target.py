
'''
Print out if the list can sum to target
'''

def sum_target(target, list):
    ans = False
    for i in list:
        for j in list:
            if (i+j) == target:
                ans = True
    return ans

alist = [5,3,5,7,1,2,5,6]
print a, sum_target(20, alist)

def sum_target2(target, list):
    if list <= 1 and list[0] != target:
        return False
    if (list[-2]+list[-1]) == target:
        return True
    else:
        return sum_target2(target, list[:-1])

print 2, sum_target(8, alist)
