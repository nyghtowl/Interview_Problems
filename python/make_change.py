#!/usr/bin/env python
'''
Make Change 
(variation on sum target question but more than pair)

Input: Target coin and list of coins
Output: Count of unique ways to make change OR
        List of unique ways to make change - originally coded by Jasmine

'''

#Count solution
def make_change(coins, num_coins, target):
    count = 0

    if target == 0:
        return 1
    
    if target < 0:
        return 0

    if num_coins <= 0 and target >= 1:
        return 0

    return make_change(coins, num_coins-1, target) + make_change(coins, num_coins, target - coins[num_coins-1])
    

#Recursive solution to return all unique combinations of change to make taret
#Solution applies dynamic programming


#global variable - bad but whatever
amts_calculated = {0 : ([0, 0, 0, 0],)} #default combination for zero cents is zero coins across


def make_change2(target):

    if target < 0 :
        return []

    if target == 0 :
        return amts_calculated[0]

    if target not in amts_calculated:
        combined_list = ()

        for index, coin in enumerate(coins):
            base_solutions_list = make_change2(target-coin)
            solutions_list = ()

            for solution in base_solutions_list:
                new_solution = solution[:]
                new_solution[index] += 1

                solutions_list = solutions_list + (new_solution,)

            for new_solution in solutions_list:
                if new_solution not in combined_list:
                    combined_list = combined_list + (new_solution,)

        amts_calculated[target] = combined_list

    return amts_calculated[target]


# Test section

coins = [1, 5, 10, 25]
num_coins = len(coins)
print num_coins

target = 1
target2 = 2
target3 = 3
target4 = 5
target5 = 7
target6 = 10
target7 = 25
target8 = 27

result = 1
result2 = 1
result3 = 1
result4 = 2
result5 = 2
result6 = 4
result7 = 13
result8 = 13

implementations = [make_change]

for impl in implementations:
    print "trying %s" % impl
    print "  f(%s) == %s: %s" % (target, result, impl(coins,num_coins,target) == result)
    print "  f(%s) == %s: %s" % (target2, result2, impl(coins,num_coins,target2) == result2)
    print "  f(%s) == %s: %s" % (target3, result3, impl(coins,num_coins,target3) == result3)
    print "  f(%s) == %s: %s" % (target4, result4, impl(coins,num_coins,target4) == result4)
    print "  f(%s) == %s: %s" % (target5, result5, impl(coins,num_coins,target5) == result5)
    print "  f(%s) == %s: %s" % (target6, result6, impl(coins,num_coins,target6) == result6)
    print "  f(%s) == %s: %s" % (target7, result7, impl(coins,num_coins,target7) == result7)
    print "  f(%s) == %s: %s" % (target8, result8, impl(coins,num_coins,target8) == result8)

result1_2 = ([1,0,0,0],)
result2_2 = ([2,0,0,0],)
result3_2 = ([3,0,0,0],)
result4_2 = ([5,0,0,0],[0,1,0,0])
result5_2 = ([7,0,0,0],[2,1,0,0])
result6_2 = ([10, 0, 0, 0], [5, 1, 0, 0], [0, 2, 0, 0], [0, 0, 1, 0])
result7_2 = ([25, 0, 0, 0], [20, 1, 0, 0], [15, 2, 0, 0], [15, 0, 1, 0], [10, 3, 0, 0], [10, 1, 1, 0], [5, 4, 0, 0], [5, 2, 1, 0], [5, 0, 2, 0], [0, 5, 0, 0], [0, 3, 1, 0], [0, 1, 2, 0], [0, 0, 0, 1])
result8_2 = ([27, 0, 0, 0], [22, 1, 0, 0], [17, 2, 0, 0], [17, 0, 1, 0], [12, 3, 0, 0], [12, 1, 1, 0], [7, 4, 0, 0], [7, 2, 1, 0], [7, 0, 2, 0], [2, 5, 0, 0], [2, 3, 1, 0], [2, 1, 2, 0], [2, 0, 0, 1])

implementations2 = [make_change2]
for impl in implementations2:
    print "trying %s" % impl
    print "  f(%s) == %s: %s" % (target, result1_2, impl(target) == result1_2)
    print "  f(%s) == %s: %s" % (target2, result2_2, impl(target2) == result2_2)
    print "  f(%s) == %s: %s" % (target3, result3_2, impl(target3) == result3_2)
    print "  f(%s) == %s: %s" % (target4, result4_2, impl(target4) == result4_2)
    print "  f(%s) == %s: %s" % (target5, result5_2, impl(target5) == result5_2)
    print "  f(%s) == %s: %s" % (target6, result6_2, impl(target6) == result6_2)
    print "  f(%s) == %s: %s" % (target7, result7_2, impl(target7) == result7_2)
    print "  f(%s) == %s: %s" % (target8, result8_2, impl(target8) == result8_2)
