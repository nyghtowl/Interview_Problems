#!/usr/bin/env python
'''
Find Duplicates

Input: list of Size N, integers from 1 to n
Output: print out if there are duplicates
'''

#O(n)
def find_dup(list1):
    count = {}
    ans = []
    for l in list1:
        count.setdefault(l,0)
        count[l]+=1
    for item, num in count.iteritems():
        if num > 1:
            ans.append(item) 
    return ans

#O(n)
def find_dup2(list1):
    ans = []
    for i,l in enumerate(list1):
        if i < len(list1):
            if l in list1[i+1:]:
                ans.append(l) 
    ans.sort()
    return ans


if __name__ == '__main__':
    #Test section
    implementations = [find_dup,find_dup2]
    input1 = [5,4,7,2,1,8,3,1,4]
    result1 = [1, 4]

    for impl in implementations:
        print "  f(%s) == %s: %s" % (input1, result1, impl(input1) == result1)
