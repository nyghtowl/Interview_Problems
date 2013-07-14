#!/usr/bin/env python
'''
Palindrome Part 2 

Input: List of words
Output: Rearrange each word if can be a palindrome, otherwise replace with -1 and return the list

'''

from collections import deque, defaultdict
from palindrome import pal2 # path relative import - pull from Github python folder

#Use deque structure to solve.
def palindrome(words):
    pal_list = []
    if len(words) <= 1 and len(words[0]) <= 1 :
        pal_list.append(''.join(words))
        
    #Loop through words.
    for i, word in enumerate(words):
        
        #Create count of letters.
        counter = {}
        for j,letters in enumerate(word): 
            counter[letters] = counter.get(letters, 0) + 1
        
        #Loop through counter and assign letters to deque
        sides = []
        center = deque()
        for letter, occurrences in counter.items():
            quotiant, remainder = divmod(occurrences, 2)

            if not remainder:
                sides.append(letter * quotiant)
                continue

            if center:
                pal_list.append(-1)
                sides = []        
                center = deque()
                break

            center.append(letter * occurrences)

        center.extendleft(sides)
        center.extend(sides)

        if center != deque([]):
            pal_list.append(''.join(center))

    return pal_list


#Build dictionary of letter counts, then build word if only 1 occurance of an odd count
def palindrome2(words_list):
    pal_list = []
    for i, word in enumerate(words_list):

        #Build dictionary of letter counts:
        count_dict = {}
        for j, letter in enumerate(word):

            if letter in count_dict:
                count_dict[letter] += 1
            else:
                count_dict[letter] = 1

        #Find number of odd letter occurances in dictionary
        remainder = 0
        for key, value in count_dict.iteritems():
            if value % 2 != 0:
                remainder +=1

        if remainder > 1:
            pal_list.append(-1)
        else:
            sides = []
            middle = []   
        
            for key, value in count_dict.iteritems():
                if value % 2 == 0:
                    sides.append(key * (value/2))
                else:
                    middle.append(key * value)
            
            if sides:
                middle.extend(sides)
                middle.reverse()
                middle.extend(sides)
            
            if middle != -1:
                pal_list.append(''.join(middle))

    return pal_list


def palindrome3(words_list):
    results = []
    def fail():
        results.append(-1)

    def count_occurrences(word, evens, odds):
        for c in word:
            # count letters but also swap them back and forth for easy checking
            # of the # of odds later.
            if c in odds:
                left = evens
                right = odds
            else:
                left = odds
                right = evens

            left[c] = right[c] + 1
            del right[c]

    for word in words_list:
        evens = defaultdict(int)
        odds = defaultdict(int)
        count_occurrences(word, evens, odds)

        # if the word is len-even, then there must
        # be no odd-occurring letters - otherwise it can't be
        # a palindrome.
        if len(word) % 2 == 0:
            if len(odds) != 0:
                fail()
                continue
            center = ""
        else:
            # ok, odd-length, but still we must have only one odd.
            if len(odds) > 1:
                fail()
                continue
            # fancy: center = odds.keys()[0] * odds.values()[0]
            center_letter, center_count = odds.items()[0]
            center = center_letter * center_count
        # build the left half, then join it to the center and the left's reverse:
        left = []
        for char, count in evens.items():
            left.append(char * (count/2))
        left = "".join(left)
        # and that's a final palindrome:
        results.append(left + center + left[::-1])
    return results

if __name__ == '__main__':
    #Test section.
    implementations = [palindrome, palindrome2, palindrome3]
    words = ['cecarar', 'nono', 'abbbbb']
    words2 = ['talliat', 'eded', 'memo']
    words3 = ['hello']
    words4 = ['']

    result = ['rcaeacr', 'noon', -1]
    result2 = ['ltaiatl', 'deed', -1]
    result3 = [-1]
    result4 = ['']

    #Function to check if its a palindrome despite the order of the letters.
    def verify(actual, expected):
        for i, val in enumerate(actual):
            if val == -1:
                if expected[i] != -1:
                    return False
                continue
            if pal2(val) != pal2(expected[i]):
                return False
        return True

    for impl in implementations:
        print "trying %s" % impl
        print "  f(words1) == result: %s" % (verify(impl(words), result))
        print "  f(words2) == result2: %s" % (verify(impl(words2), result2))
        print "  f(words3) == result3: %s" % (verify(impl(words3), result3))
        print "  f(words4) == result4: %s" % (verify(impl(words4), result4))
