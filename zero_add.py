'''
process a list of numbers and return each pair of numbers that adds up to zero 
'''

ex = [0,-1,5,0,3,1]


def sum_zero(ex):
    pairs = []
    for index, elem in enumerate(ex):
        # for i in range(len(ex[index+1:])):
        for i in ex[index+1:]:
            if (elem + i) == 0:
                pairs.append((elem, i))
    return pairs


print sum_zero(ex)


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
#         return l[0] + sum_recursive(l[1:]) == 0
 

# len(l) = 5
# l[0] = 0
# l[1] = -1
# l[1:] = [-1, 5, 3, 1]
# l[0] + sum_recursive = ?

# len(l) = 4



# target = 0



# pick and hold 1 element and loop through the rest of the list and add to compare if works

def return_list(l):
    pairs = []
    for index, val in enumerate(l):
        pairs.append(compare_val(val, l[index+1:]))
    return pairs

def compare_val(target,sub_list):
    for i in sub_list:
        if sum_zero(target,i):
    return (target, i)

def sum_zero(num_1, num_2):
    return (num_1 + num_2 == 0)