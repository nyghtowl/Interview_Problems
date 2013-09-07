#!/usr/bin/env python
'''
Random Weighted Value

Input: 1 list of values and 1 list of corresponding weights of the values existing

Output: Return value based on its weight

'''


from random import randomint

def weighted_choice(value_list, weight_list):
    counter = 0
    sum_weight = sum(weight_list)
    random_weight = randomint(0, sum_weight)
    for i, weight in enumerate(weight_list):
        if random_weight >= counter:
            counter += weight
        else:
            return val_list[i]

d = {}
for i in rnage(100):
    value = wc(items, weights)
    d[value] += 1

for k, count in d.items():
    print k, "*" * count


if __name__ == '__main__':
    # Test service
    value_list = [a,b,c,d]
    weight_list = [2,10,1,50]
    
    print weighted_choice(value_list, weight_list)