#!/usr/bin/env python
"""
Give a list of strings, return another list of anagram sets.
Example:
    Input: ['cat', 'tablet', 'wolf', 'act', 'battle', 'flow', 'batlet', 'food']
    Output: [['cat', 'act'], ['tablet', 'battle', 'batlet'], ['wolf', 'flow']]
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

    for k, v in matches.items():
        if len(v) >= 2:
            results.append(v)

    return results


if __name__ == '__main__':
    print anagram(['cat', 'tablet', 'wolf', 'act', 'battle', 'flow', 'batlet',
                    'food'])

