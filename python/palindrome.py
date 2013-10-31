#!/usr/bin/env python
'''
Palindrome

Input: word
Output: true if a palindrome

Note: jofusa contributed additional example and test
'''

#Recursive solution.
def pal(word):
    if len(word) < 2:
        return True
    if word[0] == word [-1]:
        return pal(word[1:-1])
    if word[0] != word [-1]:
        return False

#Simple reverse list solution. O(n)
def pal2(word):
    return word == word[::-1]


#Strip out space and uppercases. O(n)
def pal3(word):
    stripped_word = word.replace(' ','').lower()
    return stripped_word == stripped_word[::-1]

def palWrapper(str1, str2):
    # A single-length string cannot be semordnilap
    if len(str1) == 1 or len(str2) == 1:
        return False

    # Equal strings cannot be semordnilap
    if str1 == str2:
        return False

    return pal4(str1, str2)

#Solve by skipping over spaces and punctuation
def pal4(str1, str2):

    # If strings aren't the same length, they cannot be palindrome
    if len(str1) != len(str2):
        return False

    # Base case: if the strings are each of length 1, check if they're equal
    if len(str1) == 1:
        return str1 == str2

    # Recursive case: check if the first letter of str1 equals the last letter of str2    
    if str1[:1] == str2[-1:]:
        return pal4(str1[1:], str2[:-1])
    else:
        return False


if __name__ == '__main__':
    #Test
    s = 'rowme'
    s2 = 'Lion oil'
    s3 = 'a man a plan a canal Panama'
    s4 = ('live', 'evil')
    s5 = ('dog', 'god')
    s6 = ('a', 'at')
    s7 = ('qanukywtmjcevo', 'hldxsgrtvkeywj')

    answers = ['emwor','lio noiL', 'amanaP lanac a nalp a nam a', True, True, False]

    result = False
    result2 = True

    implementations = [pal,pal2,pal3]
    implementations2 = [pal3]
    implementations3 = [palWrapper]

    for impl in implementations:
        print "trying %s" % impl
        print "f(s) == %s: %s" % (result,(impl(s) == result))

    for impl in implementations2:
        print "f(s2) == %s: %s" % (result2,(impl(s2) == result2))
        print "f(s3) == %s: %s" % (result2,(impl(s3) == result2))

    for impl in implementations3:
        print "f(s4) == %s: %s" % (result2,(impl(s4[0],s4[1]) == result2))
        print "f(s5) == %s: %s" % (result2,(impl(s5[0],s5[1]) == result2))
        print "f(s6) == %s: %s" % (result,(impl(s6[0],s6[1]) == result))
        print "f(s7) == %s: %s" % (result,(impl(s7[0],s7[1]) == result))
