#!/usr/bin/env python
'''
Sentence Sort Test

Test file for sentence_sort problem

Original problem/solution submission from jofusa
'''

from sentence_sort import *

def test_sentence_sort():
    test = "This is the First"
    assert "is the This First" ==  pythonic_approach(test)

