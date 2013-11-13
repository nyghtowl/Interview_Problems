'''
String Lacing

s1 and s2 are strings.

Returns a new str with elements of s1 and s2 interlaced,
beginning with s1. If strings are not of same length, 
then the extra elements should appear at the end.
'''


def laceStrings(s1, s2):
    size = min(len(s1), len(s2))
    longest_str = max(s1,s2)
    result = ''

    for i in range(size):
        result += s1[i] + s2[i]
    
    return result + longest_str[size:]

def laceStringsRecur(s1, s2):

    def helpLaceStrings(s1, s2, out):
        if s1 == '':
            return s2
        if s2 == '':
            return s1
        else:
            return s1[0] + s2[0] + helpLaceStrings(s1[1:], s2[1:], '')
            # return  out + helpLaceStrings(s1[1:], s2[1:], s1[0] + s2[0])

    return helpLaceStrings(s1, s2, '')

if __name__ == '__main__':

    # Test section    
    test_func = laceStrings
    string1 = ['abcd', '  ', 'ttt', '', 'and', 'treehousego']
    string2 = ['efghi', 'abc', 'ccc', '', 'treehousego', 'a']
    results = ['aebfcgdhi', ' a bc', 'tctctc', '', 'atnrdeehousego', 'tareehousego']

    for i in range(len(results)):
        print "trying %s" % test_func
        print "f(%s, %s) == %s: %s" % (string1[i], string2[i], results[i], test_func(string1[i],string2[i]) == results[i])
        print test_func(string1[i],string2[i])
