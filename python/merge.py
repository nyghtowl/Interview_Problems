#!/usr/bin/env python
'''
Mergesort 

Input: words
Output: sorted array of items in O(n log n)

Challenge:
    How to complete mergesort in constant space?
'''
from random import shuffle


# Check input type and convert to list.
def mergesort(words):
    if type(words) is str:
        result = slice_array(list(words))
        return ''.join(result)
    else:
        return slice_array(words)


# Determine input len & splits and call merge function.
def slice_array(mlist):
    size = len(mlist)
    if size <= 1: 
        return mlist
    mid = size / 2
    return sort_values(slice_array(mlist[:mid]), slice_array(mlist[mid:]))


def sort_values(left, right):
    result = []
    i, j = 0, 0
    
    # Compare left and right lists and append to temp list.
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Add remaining input to results to pass back.
    return result + left[i:] + right[j:]


if __name__ == '__main__':
    # Test string.
    print mergesort('hellow world')     # ' dehllloorww'

    # Test array of ints.
    nums = [i for i in range(42)]
    shuffle(nums)
    print mergesort(nums)

