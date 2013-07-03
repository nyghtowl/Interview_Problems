'''
Quicksort Example
'''

import random

def quick_sort(l):
    if l == []:
        return []
    else:
        pivot = l[0]
        lesser = quick_sort([x for x in l[1:] if x < pivot])
        greater = quick_sort([x for x in l[1:] if x > pivot])
        return lesser + [pivot] + greater


def find_pivot(l):
    pivot_index = random.randint(0,len(l)-1)
    return pivot_index

def quick_sort2(l, length=None):
    if len(l) <= 1:
        return l
    pivot_index = find_pivot(l)
    pivot = l[pivot_index]
    #swap pivot to first item in list
    i = j = 1
    for num in l:
        if num < pivot:
            l[i],l[j]=l[j],l[i]
            i += 1
        j += 1
    l[0],l[i]=l[i],l[0]
    quick_sort2(l, i) 
    quicksort2(l, len(l)-1)
    return l # l will be changed as it goes through thus no = needed

def quick_sort3(l):
    left = right = []
    if len(l) <= 1:
        return l 
    else:
        pivot = random.randint(len(l))
        for num in l:
            if num > l[pivot]:
                left.append(l)
            else:
                right.append(l)
    return quick_sort3(left) + quick_sort3(right)

#Tests
l = [5,8,3,1,2,7,9,6]
result = [1,2,3,5,6,7,8,9]

implementations = [quick_sort, quick_sort2, quick_sort3]

for impl in implementations:
    print "trying %s" % impl
    print "%s == %s" % (impl,result)

