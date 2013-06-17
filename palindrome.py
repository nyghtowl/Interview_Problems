'''
Retun true if a palindrome
'''

#palandromes / symmetry
def pal(word):
    if len(word) < 2:
        return True
    if word[0] == word [-1]:
        return pal(word[1:-1])
    if word[0] != word [-1]:
        return False

print pal('rowme')

def pal2(word):
    return word == word[::-1]

print pal2('rowme')
