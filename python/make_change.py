'''
Make Change 
(variation on sum target question but more than pair)

Input: Target coin and list of coins
Output: Count of unique ways to make change OR
        List of unique ways to make change

'''

#Count solution - needs to be finished
def make_change(coins, target):
    count = 0

    if target < 0:
        return 0
    elif target == 0:
        return 1
    else:
        for coin in coins:
            remaining = target-coin
            count += make_change(coins, remaining)
    return count


#Recursive solution to return all unique combinations of change to make taret
#Solution applies dynamic programming and originally coded by Jasmine

coins = [25, 10, 5, 1]
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


# # Test section
# print make_change(all_coins, 1) == 1
# print make_change(all_coins, 2) == 1
# print make_change(all_coins, 3) == 1
# print make_change(all_coins, 5) == 2
# print make_change(all_coins, 7) == 2
# print make_change(all_coins, 10) == 4 # dime, 2 nickles, 1 nickle + 5 pennies, 10 pennies
# print make_change(all_coins, 25) == 12 #q, 2d1n, 2d5p, 1d3n, 1d2n5p, 1d15p, 5n, 4n5p, 3n10p, 2n15p, 1n20p, 0n25p
# print make_change(all_coins, 27) == 12

coins = [1, 5, 10, 25]
target = 10
target2 = 25

result = 4
result2 = 12

implementations = [make_change]

for impl in implementations:
    print "trying %s" % impl
    print "  f(%s) == %s: %s" % (target, result, impl(coins,target) == result)
    print "  f(%s) == %s: %s" % (target2, result2, impl(coins,target2) == result2)
    print impl(coins,target)
    print impl(coins,target2)

result3 = ([10, 0, 0, 0], [5, 1, 0, 0], [0, 2, 0, 0], [0, 0, 1, 0])
result4 = ([25, 0, 0, 0], [20, 1, 0, 0], [15, 2, 0, 0], [15, 0, 1, 0], [10, 3, 0, 0], [10, 1, 1, 0], [5, 4, 0, 0], [5, 2, 1, 0], [5, 0, 2, 0], [0, 5, 0, 0], [0, 3, 1, 0], [0, 1, 2, 0], [0, 0, 0, 1])


implementations2 = [make_change2]
for impl in implementations2:
    print "trying %s" % impl
    print "  f(%s) == %s: %s" % (target, result3, impl(target) == result3)
    print "  f(%s) == %s: %s" % (target2, result4, impl(target2) == result4)
