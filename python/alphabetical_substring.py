#!/usr/bin/env python
''' 
Alphabetical substring

Input: string
Output: the sub string that has the most characters in a row that are in alphabetical order. If there is a tie then print the first occurance.

Pulled from edx CompSci 101

'''

def alphabetical_substring(s):
    substring = {}
    max_value = 0

    for i in range(len(s)):
        count = 0
        sub_value  = s[i]

        while i+1 < len(s) and s[i] <= s[i+1]:
            count += 1
            i += 1
            sub_value += s[i]

        substring[count] = substring.get(count, sub_value)
        max_value = max(substring.keys())
    
    return substring[max_value]
    # print('Longest substring in alphabetical order is: %s' % substring[max_value])

if __name__ == '__main__':
    #Test section
    input_case = ['azcbobobegghakl', 'abcdefghijklmnopqrstuvwxyz', 'nqlkcvjkwytg', 'bovgfeiromsncq']
    ans = ['beggh', 'abcdefghijklmnopqrstuvwxyz', 'jkwy', 'bov']

    for i in range(len(input_case)):
        print('Expected input = %s and output = %s which is %s' % (input_case[i], ans[i], ans[i] == alphabetical_substring(input_case[i])))
