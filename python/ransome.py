'''
Find if a smaller string exists and/or can be created out of a larger string
'''

#Ransome note example find out if the letters are in the mag
def mag_dict(magazine):
    mag_hash = {}
    for i in magazine:
        mag_hash[i] = mag_hash.get(i, 0) + 1
    return mag_hash


def comparison(note, mag):
    mdict = mag_dict(mag)
    for i in note:
        if i in mdict:
            mdict[i] -= 1
        else:
            return False
    return True

print 8, comparison('hash', 'this is a hash')



def strstr(needle, haystack):
    pass

