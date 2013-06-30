'''
Palindrome Part 2 

Input: List of words
Output: Rearrange each word if can be a palindrome, otherwise replace with -1 and return the list

'''



from collections import deque

#Use deque structure to solve.
def palindrome(words):
    pal_list = []
    if len(words) <= 1 and len(words[0]) <=1:
        pal_list.append(words)
    
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


#Test section.
implementations = [palindrome, palindrome2]
words = ['cecarar', 'nono', 'abbbbb']
words2 = ['talliat', 'eded', 'memo']
words3 = ['hello']

result = ['rcaeacr', 'noon', -1]
result2 = ['ltaiatl', 'deed', -1]
result3 = [-1]

for impl in implementations:
    print "trying %s" % impl
    print "  f(words1) == result: %s" % (impl(words) == result)
    print "  f(words2) == result2: %s" % (impl(words2) == result2)
    print "  f(words3) == result3: %s" % (impl(words3) == result3)

