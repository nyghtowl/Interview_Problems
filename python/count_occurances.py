#!/usr/bin/env python
''' 
String Count

Input: string or array
Output: Highest count of occurances of letters in a string OR count of numbers in a list given a target OR count of occurances of a substring in a full string.

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
def list_count(num_list, n):
    count = 0
    if len(num_list) <= 1 and num_list[0] == n:
        count += 1      
    if n in num_list and len(num_list) > 1:
        pivot = int(len(num_list)/2)
        if num_list[pivot] == n:
            count += 1
            if num_list[pivot+1] == n:
                count += 1
            if num_list[pivot-1] == n:
                count += 1
        if num_list[pivot] > n:
            count += list_count(num_list[:pivot], n)
        if num_list[pivot] < n:
            count += list_count(num_list[pivot+1:], n)
    return count

#Simple solution for count numbers - O(n)
def list_count2(num_list, n):
    return num_list.count(n)

#O(n)
def list_count3(num_list, n):
    num_counts = dict((num, num_list.count(n)) for num in num_list)
    return num_counts[n]


# O(n^2) - Counting how often a sub-string appears in a full_string
def count_substr(full_string, str_match):
    num = 0
    for i, letter in enumerate(full_string):
        if letter == str_match[0]:
            j = 0
            match_case = True
            while match_case:
                if j == 3:
                    num += 1
                    match_case = False
                elif str_match[j] == full_string[i]:
                    i += 1
                    j += 1
                    if i < len(full_string):
                        continue
                    else:
                        i -= 1
                else:
                    match_case = False
    print("Number of times bob occurs is: %d" % num)
    return num

# O(n)
def count_substr2(full_string, str_match):
    occurance = 0
    for i in range(1, len(full_string)-1):
        if full_string[i-1:i+(len(str_match)-1)] == str_match:
            occurance += 1
    print 'Number of times bob occurs is:', occurance
    return occurance


# Trying something with boyers here - in progress
# def count_substr(full_string, str_match):
#     occurance = 0
#     for i in range(len(full_string),1,-len(str_match)):
#         if str_match[i]==match[-1]:
#             if full_string[i-(len(str_match)-1):i] == str_match:
#                 occurance += 1
#         elif str_match[i] in match:
#     print 'Number of times bob occurs is:', occurance
#     return ocurrance

if __name__ == '__main__':
    #Test section
    implementations = [list_count,list_count2,list_count3]
    implementations2 = [count_substr, count_substr2]
    num_list = [2,4,5,5,5,6,7]


    for impl in implementations:
        print "trying %s" % impl
        print "  f(%s, 7) == 1: %s" % (num_list, (impl(num_list,7) == 1))
        print "  f(%s, 5) == 3: %s" % (num_list, (impl(num_list,5) == 3))

    print "f(%s) == %s : %s" % ('hello world', 3, (high_occ('hello world') == 3))

    for impl in implementations2:
        print "trying %s" % impl
        print("count_substr('pupbhb', 'bob') == 0: %s") % ( impl('pupbhb', 'bob') == 0)
        print("count_substr('bobbobooflubobbbobobbobbbobbwwboobcbobbbobobcboob', 'bob') == 10: %s") % (impl('bobbobooflubobbbobobbobbbobbwwboobcbobbbobobcboob', 'bob') == 10)
        print("count_substr('mtbobbboboba', 'bob') == 3: %s") % ( impl('mtbobbboboba', 'bob') == 3)
