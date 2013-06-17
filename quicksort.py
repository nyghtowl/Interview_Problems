'''
quicksort example
'''

def quicksort(list):
    if blist == []:
        return []
    else:
        pivot = blist[0]
        lesser = qsort([x for x in blist[1:] if x < pivot])
        greater = qsort([x for x in blist[1:] if x > pivot])
        return lesser + [pivot] + greater


l = [5,8,3,1,2,7,9,6]

def find_pivot(lenz):
    pivot_index = random.randint(0,len(l)-1)
    return pivot_index

def quick_sort2(l, start, lenz):
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
    quick_sort2(l, 0, i) 
    quicksort2(l, i, len(l)-1)
    return l # l will be chagned as it goes through thus no = needed

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
