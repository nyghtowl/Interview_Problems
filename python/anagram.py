#!/usr/bin/env python
"""
Anagram 
(A word, phrase, or name formed by rearranging the letters of anothe)

Give a list of strings, return a list of anagram sets just from the original input.

Example:
    Input: ['cat', 'tablet', 'wolf', 'act', 'battle', 'flow', 'batlet', 'food']
    Output: [['cat', 'act'], ['tablet', 'battle', 'batlet'], ['wolf', 'flow']]

Note: It does not generate any new words that are not in the input.

Original problem/solution submission from claudiay
"""

def anagram(words):
    results = []
    matches = {}

    # Create a dict with sorted values as key, and list of original strings as
    # the value.
    for word in words:
        key = ''.join(sorted(list(word)))
        if matches.get(key, False):
            matches[key].append(word)
        else:
            matches[key] = [word]

    #Creates result list of lists 
    for k, v in matches.items():
        if len(v) >= 2:
            results.append(v)

    return results


def anagram2(words):
    matches = {}

    # Create a dict with sorted values as key, and list of original strings as
    # the value.
    for word in words:
        key = ''.join(sorted(list(word)))
        if matches.get(key, False):
            matches[key].append(word)
        else:
            matches[key] = [word]

    #Pops value from dict if not more than 1 and returns dictionary values
    for k, v in matches.items():
        if len(v) <= 1:
            matches.pop(k, None)

    return matches.values()

if __name__ == '__main__':

    #Test
    implementations = [anagram,anagram2]

    words_input = ['cat', 'tablet', 'wolf', 'act', 'battle', 'flow', 'batlet', 'food']
    result = [['tablet', 'battle', 'batlet'], ['wolf', 'flow'], ['cat', 'act']]

    for impl in implementations:
        print "trying %s" % impl
        print "  f(%s) returns %s: %s" % (words_input,result,(impl(words_input) == result))



