'''
Palindrome

Input: word
Output: true if a palindrome
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

#Solve by skipping over spaces and punctuation
def pal3(word):
    pass
    '''
    kept a cursor on the left (start from 0) and a cursor on the right (start from len(string)-1) (increment and decrease the left & right indices respectively if not valid), check if they are equal, and basically do it until the two cursors have crossed over (where right < left)> 
    '''

#Strip out space and uppercases. O(n)
def pal4(word):
    stripped_word = word.replace(' ','').lower()
    return stripped_word == stripped_word[::-1]

#Test
s = 'rowme'
s2 = 'Lion oil'
s3 = 'a man a plan a canal Panama'

result = False
result2 = True

implementations = [pal,pal2,pal4]
implementations2 = [pal4]

for impl in implementations:
    print "trying %s" % impl
    print "f(s) == %s: %s" % (result,(impl(s) == result))

for impl in implementations2:
    print "f(s2) == %s: %s" % (result2,(impl(s2) == result2))
    print "f(s3) == %s: %s" % (result2,(impl(s3) == result2))
