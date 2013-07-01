'''
Retun true if a palindrome
'''

#Recursive solution
def pal(word):
    if len(word) < 2:
        return True
    if word[0] == word [-1]:
        return pal(word[1:-1])
    if word[0] != word [-1]:
        return False

#Simple reverse list solution
def pal2(word):
    return word == word[::-1]

#Solve by skipping over spaces and punctuation
def pal3(word):
    pass
    '''
    kept a cursor on the left (start from 0) and a cursor on the right (start from len(string)-1) (increment and decrease the left & right indices respectively if not valid), check if they are equal, and basically do it until the two cursors have crossed over (where right < left)> 
    '''


print pal2('rowme')

