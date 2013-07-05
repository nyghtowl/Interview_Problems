'''
make change 


'''
coins = [1, 5, 10, 25]
target = 100

# def chg_count(coins, target):
#     count = 0
#     if target < 0:
#         return
#     if target == 0:
#         return 1
#     if target > 0:
#         for i in coins:
#             if target -i >= 0:
#                 count += chg_count(coins, target-i)
#     return count

# # print 15, chg_count(coins, target)

# # make change - how many combinations of the change make up a target
# coins = [1, 5, 10, 25]
# target = 5.17

# def chg_count(coins, target):
#     count = None
#     if target < 0:
#         return
#     if target == 0:
#         return 1
#     if target > 0:
#         for i in list:
#             if target -i >= 0:
#                 count += chg_count(coints, target-i)
#     return count


'''
set.add(#) - pulls unique out of list and allows that you don't count multiple versions
when 0 - add set to dict to count the unique combinations
or nested set
'''

# def make_change(coins, target):
#     print "making change for %s target" % target
#     count = 0
#     if len(coins) > 0:
#         if target < 0:
#             return
#         elif target == 0:
#             return 1
#         else:
#             for coin in coins:
#                 if coin <= target:
#                     remaining = target-coin
#                     if remaining >= 0:
#                         print "using %s coin, %s remaining" % (coin, remaining)
#                         count += make_change(coins, remaining)
#     return count

# 25, 10, 5, 1
# 10
# 1d 2n 1n5p 10p
# 1q 2d1n 2d5p 1d3n 1d2n5p 1d1n10p 1d0n15p 5n 4n5p 3n10p 2n15p 1n20p 25p

# return a list of coins that make the target change but don't return duplicates

# def make_change(coins, target):
#     # print "making change for %s target" % target
#     result = {}
#     # if target is <= 0 return empty list
#     if target > 0:
#     # track full combo of coins and add to a list when target = 0
#         coin_target = target # problem with reseting
#         # go through coin list and pull index and coins        
#         for index, coin in enumerate(coins):
#             coin_combo = make_solution_template()
#             occurances = int(target/coin)            
#             if occurances < 1:
#                 break
#             if occurances == 0:
#                 coin_combo[index] = occurances
#                 print 2, coin_target
#             elif occurances == 1:
#                 coin_target -= coin
#                 coin_combo[index] = 1
#                 for i, c in enumerate(coins[index+1:]):
#                     if coin_target%c == 0:
#                         coin_combo[i] = int(coin_target/c)
#                     elif coin_target/c >= 1:
#                         coin_target -= int(coin_target/c)
#                         coin_combo[i] = int(coin_target/c)                
#             else:
#                 coin_target -= occurances
#                 coin_combo[index] = occurances

#                 for i, c in enumerate(coins[index+1:]):
#                     if coin_target%c == 0:
#                         coin_combo[i] = int(coin_target/c)
#                     elif coin_target/c >= 1:
#                         coin_target -= int(coin_target/c)
#                         coin_combo[i] = int(coin_target/c)
#             coin_combo = tuple(coin_combo)
#             if coin_combo not in result and coin_combo != (0,0,0,0):
#                 result[coin_combo] = 1  
#     print result.keys()
#     print len(result.keys())
#     return len(result.keys())



def make_solution_template(num_coins=4):
    return [0] * num_coins

def make_change(coins, target):
    result = {}
    if target > 0:
        coin_target = target 
        for index, coin in enumerate(coins):
            coin_combo = make_solution_template()
            occurances = int(target/coin)            
            if occurances < 0:
                break
            if occurances == 0:
                coin_combo[index] = occurances
            else:
                coin_target -= occurances
                coin_combo[index] = occurances
                if occurances > 1:
                    for num in range(occurances,0):
                        for i, c in enumerate(coins[index+1:]):
                            if coin_target%c == 0:
                                coin_combo[i] = int(coin_target/c)
                            elif coin_target/c >= 1:
                                coin_target -= int(coin_target/c)
                                coin_combo[i] = int(coin_target/c)
                else:
                    for i, c in enumerate(coins[index+1:]):
                        if coin_target%c == 0:
                            coin_combo[i] = int(coin_target/c)
                        elif coin_target/c >= 1:
                            coin_target -= int(coin_target/c)
                            coin_combo[i] = int(coin_target/c)
            coin_combo = tuple(coin_combo)
            if coin_combo not in result and coin_combo != (0,0,0,0):
                result[coin_combo] = 1  
    print result.keys()
    print len(result.keys())
    return len(result.keys())

#dividing by coin and for loop from number decreasing to zero range range(int(target/coin:0:-1)))
#look at rest of coins in the list to determine other options going to zero

coin_combo = [0,0,0,0]
all_coins = [25, 10, 5, 1]

# test
print make_change(all_coins, 1) == 1
print make_change(all_coins, 2) == 1
print make_change(all_coins, 3) == 1
print make_change(all_coins, 5) == 2
print make_change(all_coins, 7) == 2
print make_change(all_coins, 10) == 4 # dime, 2 nickles, 1 nickle + 5 pennies, 10 pennies
print make_change(all_coins, 25) == 12 #q, 2d1n, 2d5p, 1d3n, 1d2n5p, 1d15p, 5n, 4n5p, 3n10p, 2n15p, 1n20p, 0n25p
print make_change(all_coins, 27) == 12
