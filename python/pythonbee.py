#!/usr/bin/env python
'''
Python-bee Sample from DBX 2013

'''

'''
Input: Non-empty, unique list of integers
Output: True if list is sorted else False
'''

def f(l):
    return sorted(l) == l

'''
Input: List of integers
Output: List of their squares in same order
'''
def f2(l):
   return [i*i for i in l]

'''
Input: Non-empyt list of floats 
Output: Mean
'''
def f3(a):
    return sum(a)/len(a)

'''
Input: Non-negative integer, X 
Output: Sum of the digits of 2^x
'''

def f4(x):
    ans = 0
    for i in str(2*x):
        ans += int(i)
    return ans

'''
Input: String of letters 
Output: Length of the longest substring of that string consisting of the same letter repeated
'''
def f5(x):
    pass #To be answered

#Test section

#Input
int_list = [1,2,6,5]
float_list = [1.5,2.5,3.5]
num = 32

#Output
int_list_result = False
int_list_result2 = [1,4,36,25]
float_list_result = 2.5
sum_num_result = 10

print "f(%s) == %s: %s" % (int_list, int_list_result, f(int_list) == int_list_result)
print "f2(%s) == %s: %s" % (int_list, int_list_result2, f2(int_list) == int_list_result2) 
print "f3(%s) == %s: %s" % (float_list, float_list_result,f3(float_list) == float_list_result)
print "f4(%s) == %s: %s" % (num, sum_num_result, f4(num) == sum_num_result)
