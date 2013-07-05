'''
Subset 

Input: list of intergers and number of values to return
Output: list contains the number small values in the list
'''

#Using embeded for loops - O(n^2)
def small_sub(l,k):
    for j in range(len(l)):
        for i in range(len(l)):
            if l[j] < l[i]:
                l[i], l[j] = l[j], l[i]
    return l[0:k]

#Apply sort - O(n)
def small_sub2(l,k):
    l.sort()
    return l[0:k]

#Test
num_list = [1,10,3,9,5,-1]
num_vals = 3

implementations = [small_sub, small_sub2]
result = [-1,1,3]

for impl in implementations:
    print "trying %s" % impl
    print "  f(%s) == %s: %s" % (impl, result, impl(num_list,num_vals) == result)

print small_sub(num_list, num_vals)