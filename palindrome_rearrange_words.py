'''
Palindrome Part 2 

Input: List of words
Output: Rearrange and print if can make a palindrome

'''

#First version using deque structure and separating functions to reorder words and work through the list of words

from collections import deque

def pal(word):
    a_dict = {}
    for i,letter in enumerate(word):
        a_dict[letter] = a_dict.get(letter, 0) + 1
    if   
    print a_dict

def palindrome(words):
    for i, word in enumerate(words):
        print i, word
        counter = {}
        for j,letters in enumerate(word):
             counter[letters] = counter.get(letters, 0) + 1
        sides = []
        center = deque()
        for letter, occurrences in counter.items():
            repetitions, odd_count = divmod(occurrences, 2)
            if not odd_count:
                sides.append(letter * repetitions)
                continue
            if center:
                print "Value Error"
                center = deque()
                break
                # raise ValueError("no palindrome exists for '{}'".format(letters))
            center.append(letter * occurrences)
        center.extendleft(sides)
        center.extend(sides)
        if inner:
            print ''.join(center)
    return ' '.join(result)


#Second version to place letter count in dict and then loop back through to create palindromes.
def compute_palindromes(words_list):
    for i, word in enumerate(words_list):
        count_dict = {}
        for j, letter in enumerate(word):
            if letter in count_dict:
                count_dict[letter] += 1
            else:
                count_dict[letter] = 1
        print count_dict

        odd_count = 0
        for key, value in count_dict.iteritems():
            if value % 2 != 0:
                odd_count +=1
        if odd_count > 1:
            print -1
            return

        start = []
        end = []
        middle = None   
    
        for key, value in count_dict.iteritems():
            if value % 2 == 0:
                val = int(value)/2
                start.append(key * val)
                end.append(key * val)
            else:
                middle = key
    
        if middle:
            start.append(middle)
        end.reverse()
        start.extend(end)
        string = "".join(start)
        print string

#Test section.
pal('hello')
palindrome(['talliat', 'eded', 'memo'])
words = ["cecarar", "nono", "abbbbb"]
