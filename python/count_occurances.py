#!/usr/bin/env python
''' 
String Count

Input: string or array
Output: Highest count of occurances of letters in a string or count of
numbers in a list given a target

'''

# Count string letters in unsorted string - O(n)
def high_occ(string):
    letter_dict = {}
    high_value = 0
    for i in string:
        letter_dict[i] = letter_dict.get(i, 0) + 1
    for key, value in letter_dict.iteritems():
        if value > high_value:
            high_value = value
    return high_value


# Count numbers in a list
def list_count(hal, n):
    count = 0
    if len(hal) <= 1 and hal[0] == n:
        count += 1      
    if n in hal and len(hal) > 1:
        pivot = int(len(hal)/2)
        if hal[pivot] == n:
            count += 1
            if hal[pivot+1] == n:
                count += 1
            if hal[pivot-1] == n:
                count += 1
        if hal[pivot] > n:
            count += list_count(hal[:pivot], n)
        if hal[pivot] < n:
            count += list_count(hal[pivot+1:], n)
    return count

#Simple solution for count numbers - O(n)
def list_count2(hal, n):
    return hal.count(n)

#O(n)
def list_count3(hal, n):
    return dict((n, hal.count(n)) for n in hal)


def list_count4(hal, n):
    count = 0
    if len(hal) <= 1 and hal[0] == n:
        return 1      
    if n in hal and len(hal) > 1:
        pivot = int(len(hal)/2)
        if hal[pivot] == n:
            if hal[pivot+1] == n:
                return (count + list_count(hal[:pivot], n))
            if hal[pivot-1] == n:                
                return (count + list_count(hal[pivot+1:], n))
        if hal[pivot] > n:
            return (count + list_count(hal[:pivot], n))
        if hal[pivot] < n:
            return (count + list_count(hal[pivot+1:], n))

if __name__ == '__main__':
    #Test section
    implementations = [list_count,list_count2,list_count3,list_count4]
    num_list = [2,4,5,5,5,6,7]


    for impl in implementations:
        print "trying %s" % impl
        print "  f(%s, 7) == 1: %s" % (num_list, (impl(num_list,7) == 1))
        print "  f(%s, 5) == 1: %s" % (num_list, (impl(num_list,5) == 3))

    print "f(%s) == %s : %s" % ('hello world', 3, (high_occ('hello world') == 3))
