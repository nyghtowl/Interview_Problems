#!/usr/bin/env python
"""
Sentence Sort

Input: sentence

Output: sort a sentence by length of words

Example:

 Input:  "This is a fun interview"
 Output: "a is fun this interview"

Original problem/solution submission from jofusa
"""


def pythonic_approach(sentence):
    """
    This utilize's python's first class functions and the optional paramater to sort arrays
    """
    return ' '.join(sorted(sentence.split(), key = len))
