'''
Find if a smaller string exists and/or can be created out of a larger string



'''

#Ransome note example find out if the letters are in the mag
def mag_dict(magazine):
    mag_hash = {}
    for i in magazine:
        mag_hash[i] = mag_hash.get(i, 0) + 1
    return mag_hash


def comparison(mag, note):
    mdict = mag_dict(mag)
    for i in note:
        if i in mdict:
            mdict[i] -= 1
        else:
            return False
    return True


def strstr(needle, haystack):
    pass


#WIP - need to finish
def match(str1,str2):
    l_str1 = list(str1)
    l_str2 = list(str2)
    state = True

    #Check which string would be a subset.
    if len(l_str1) > len(l_str2):
        large_list, small_list = l_str1, l_str2
    else:
        large_list, small_list = l_str1, l_str2

    for letter in large_list:
        if letter not in small_list:
            state = False

# in progress

    return state

#Embedded loop solution. - O(n+m)
def match2(s1,s2):
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

def match3(s1,s2):
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

#Test section.
str1 = 'Cat goes crazy'
str1a = 'crazy'
str1b = 'Cat'

str2 = 'this is a hash'
str2a = 'hash'
str2b = 'not'

result = True
result2 = False

implementations = [comparison, match2, match3]

for impl in implementations:
    print "trying %s" % impl
    print "f(%s) == %s: %s" % (str1a, result, (impl(str1, str1a) == result))
    print "f(%s) == %s: %s" % (str1b, result, (impl(str1, str1b) == result))
    print "f(%s) == %s: %s" % (str2a, result, (impl(str2, str2a) == result))
    print "f(%s) == %s: %s" % (str2b, result2, (impl(str2, str2b) == result2))


