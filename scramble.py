#!/usr/bin/env python
"""
Given a .txt file of acceptable English words and a string of letters, find all
acceptable words.
Example:
    Input: 'dog'
    Output: 'dog', 'god', 'go', 'do'
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
    word = tuple(sorted(word))

    for i in range(1, len(word) + 1):
        for subset in search(word, i):
            if english.get(subset, False):
                words += english.get(subset)
    return words


if __name__ == '__main__':
    english = create_dict('words.txt')
    print "Dictionary created."
    print unscramble('dog', english)
    print unscramble('yawn', english)

