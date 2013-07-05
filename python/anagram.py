#!/usr/bin/env python
"""
Anagram 
(A word, phrase, or name formed by rearranging the letters of anothe)

Give a list of strings, return a list of anagram sets just from the original input.

Example:
    Input: ['cat', 'tablet', 'wolf', 'act', 'battle', 'flow', 'batlet', 'food']
    Output: [['cat', 'act'], ['tablet', 'battle', 'batlet'], ['wolf', 'flow']]

Note: It does not generate any new words that are not in the input
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

    words_input = ['cat', 'tablet', 'wolf', 'act', 'battle', 'flow', 'batlet', 'food']
    anagram_result = ['tablet', 'battle', 'batlet'], ['wolf', 'flow'], ['cat', 'act']


    print anagram(['cat', 'tablet', 'wolf', 'act', 'battle', 'flow', 'batlet',
                    'food'])
    print anagram2(['cat', 'tablet', 'wolf', 'act', 'battle', 'flow', 'batlet',
                    'food'])
