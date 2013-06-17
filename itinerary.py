
'''
print out the cities for itinerary in order


SFO - LAX
LAX - BOS
JFK - SFO
BOS - DEN
'''

def orig(list):
    org_dict = {}
    for i, loc in enumerate(list):
        if loc[0] in orig_dict:
            orig_dict[loc[0]].append(0)
        else:
            orig_dict[loc[0]] = [0]
        if loc[1] in orig_dict:
            orig_dict[loc[1]].append(1)
        else:
            orig_dict[loc[1]] = [1]
    return iten(orig_dict, list)

def iten(dict, list):
    for key, value in dict:
        if value == [0]:
            print key
            orig = key
            for i, loc in enumerate(list):
                if orig == loc[0]:
                    print loc[1]
                    orig = loc[1]
                    list.pop(i)