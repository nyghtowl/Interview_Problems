#!/usr/bin/env python
'''
Random Weighted Value

Input: 1 list of values and 1 list of corresponding weights of the values existing

Output: Return value based on its weight

'''
import random

#O(n)
def weighted_choice(value_list, weight_list):
    counter = 0
    sum_weight = sum(weight_list)
    random_weight = random.randomint(0, sum_weight)
    for i, weight in enumerate(weight_list):
        if random_weight >= counter:
            counter += weight
        else:
            return val_list[i]
#O(n)
def print_weight(items, weights):
    d = {}
    for i in range(100):
        value = weighted_choice(items, weights)
        d[value] += 1

    for k, count in d.items():
        print k, "*" * count

#O(n) - Jesse's answers
def weighted_choice2(choices):
    total = sum(weight for choice, weight in choices)
    r = random.uniform(0, total)
    count = 0
    for choice, weight in choices:
        if count + weight > r:
            return choice
        count += weight
 
#O(n)
def print_weight2(choices): 
    counts = {v: 0 for v, weight in values}
    for i in range(100):
        v = weighted_choice(choice)
        counts[v] += 1
     
    for v in sorted(counts.keys()):
        count = counts[v]
        print v, "*" * count

if __name__ == '__main__':
    # Test service
    value_list = [a,b,c,d]
    weight_list = [2,10,1,50]

    print print_weight(value_list, weight_list)

    values = [('a', 50),('b', 10),('c', 10),('d', 30),('e', 5),('f', 5)]

    print print_weight2(values)
