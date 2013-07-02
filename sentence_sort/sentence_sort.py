"""
sort a sentence by length of words

Example:

 Input:  "This is a fun interview"
 Output: "a is fun this interview"

"""


def pythonic_approach(sentence):
    """
    This utilize's python's first class functions and the optional paramater to sort arrays
    """
    return ' '.join(sorted(sentence.split(), key = len))
