#!/usr/bin/env python
'''
String Match
Find if a smaller string exists and/or can be created out of a larger string.

Input: Two strings
Output: True if the smaller string exists in the larger string

Known as ransome note or needle in a haystack.

'''

#Ransome note example find out if the letters are in the mag
#Split in two functions which equal nested loops - O(n^2)
def mag_dict(magazine):
    mag_hash = {}
    for i in magazine:
        mag_hash[i] = mag_hash.get(i, 0) + 1
    return mag_hash


def match(mag, note):
    mdict = mag_dict(mag)
    for i in note:
        if i in mdict:
            mdict[i] -= 1
        else:
            return False
    return True


#Check which string would be a subset assuming the order submitted changes
def find_main_str(str1, str2):
    if len(str1) > len(str2):
        return (str1, str2)
    else:
        return (str2, str1)

#O(n)
def match2(str1,str2):
    large, small = find_main_str(str1,str2)

    if small in large:
        return True


#Embedded loop solution. - O(n+m)
def match3(s1,s2):
    state = False
    for i, char in enumerate(s1):
        if s2[0] == char:
            j=0
            while j < len(s2):
                if i+j < len(s1):
                    if s2[j] != s1[i+j]:
                        break
                    else: 
                        state = True
                        j += 1
                else:
                    break
    return state

#Boyer Moore Algorithm approach - compare starting end of string 
#check each subset of the main string whether the last character is
#included. If not then shift out another subset. - O(n-m)

#Note: still not functioning properly - need to account for end of string

def match4(s1,s2):
    j_d = {}
    for c in s1:
        j_d[c] = True

    i = len(s2)-1
    while i < len(s1):
        if not j_d.get(s1[i]):
            if i >= len(s1):
                i = len(s1)-1
            else:
                i += len(s2)
        else:    
            j = len(s2)-1            
            while j >= 0: 
                found = False
                a = 0
                print 1, s2[j]
                print 2, s1[i]
                print 3, j

                if s2[j] != s1[i]:
                    break
                
                j -= 1
                i -= 1
            
            i += len(s2)-1

        if j == -1:
            found = True
            break


    return found

if __name__ == '__main__':
    #Test section
    str1 = 'Cat goes crazy'
    str1a = 'crazy'
    str1b = 'Cat'

    str2 = 'this is a hash'
    str2a = 'hash'
    str2b = 'not'

    result = True
    result2 = False

    implementations = [match, match2, match3]

    for impl in implementations:
        print "trying %s" % impl
        print "f(%s) == %s: %s" % (str1a, result, (impl(str1, str1a) == result))
        print "f(%s) == %s: %s" % (str1b, result, (impl(str1, str1b) == result))
        print "f(%s) == %s: %s" % (str2a, result, (impl(str2, str2a) == result))
        print "f(%s) == %s: %s" % (str2b, result2, (impl(str2, str2b) == result2))


