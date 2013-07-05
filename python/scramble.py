#!/usr/bin/env python
"""
Given a .txt file of acceptable English words and a string of letters, find all
acceptable words.
Example:
    Input: 'dog'
    Output: 'dog', 'god', 'go', 'do'

Two cases:
    1) Using a dict that maps a sorted tuple of letters to possible words.
        ex. d[('d', 'o', 'g')] = ['dog', 'god']
    2) Using a dict that only maps string word to True:
        ex. d['dog'] = True

What are the pros and cons of the different methods? In which situation(s)
would one be preferable over the other? Which is ~generally~ better?

Original problem/solution submission from claudiay
"""

def create_dict(file_name):
    # Create dict of acceptable words from file_name.
    # Map a tuple of the sorted lettters to acceptable words.
    words = {}
    with open(file_name) as f:
        content = f.readlines()
    for word in content:
        word = word.strip()
        key = tuple(sorted(list(word)))
        if words.get(key, False):
            # Key already exists.
            words[key].append(word)
        else:
            words[key] = [word]
    return words


def create_simple_dict(file_name):
    # Create dict that maps word to True.
    # We don't have time to sort through all these words.
    words = {}
    with open(file_name) as f:
        content = f.readlines()
    for word in content:
        word = word.strip()
        words[word] = True
    return words


def search(letters, r):
    # similar to itertools.combinations()
    # iterates through all combinations of letters for length of r
    n = len(letters)
    if r > n:
        return
    indices = range(r)
    yield tuple(letters[i] for i in indices)
    while True:
        for i in reversed(range(r)):
            if indices[i] != i + n - r:
                break
        else:
            return
        indices[i] += 1
        for j in range(i + 1, r):
            indices[j] = indices[j-1] + 1
        yield tuple(letters[i] for i in indices)


def unscramble(word, english):
    words = []
    word = sorted(word)

    for i in range(1, len(word) + 1):
        for subset in search(word, i):
            if english.get(subset, False):
                words += english.get(subset)
    return words


def permutations(letters, r):
    # Similar to itertools.permutations()
    # Shuffle through all combinations found through search(). 
    n = len(letters)
    if r > n:
        return
    indices = range(n)
    cycles = range(n, n-r, -1)
    yield ''.join(letters[i] for i in indices[:r])
    while n:
        for i in reversed(range(r)):
            cycles[i] -= 1
            if cycles[i] == 0:
                indices[i:] = indices[i+1:] + indices[i:i+1]
                cycles[i] = n - i
            else:
                j = cycles[i]
                indices[i], indices[-j] = indices[-j], indices[i]
                yield ''.join(letters[i] for i in indices[:r])
                break
        else:
            return


def unscramble_simple_dict(word, english):
    words = []
    
    for i in range(1, len(word) + 1):
        for subset in permutations(word, i):
            if english.get(subset, False):
                words.append(subset)
    return words


if __name__ == '__main__':
    english = create_dict('words.txt')
    print "Dictionary created."
    print unscramble('dog', english)
    print unscramble('yawn', english)

    english = create_simple_dict('words.txt')
    print "Dictionary created."
    print unscramble_simple_dict('dog', english)
    print unscramble_simple_dict('yawn', english)

