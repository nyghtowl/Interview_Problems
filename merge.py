'''
merge sort python example

how to do in constant space?
'''
# checks input type and converts to list
def msort(words):
    if type(words) is str:
        result = merge_sort(list(words))
        return ''.join(result)
    else:
        return merg_sort(words)

# determines input len & splits and calls merge function
def merge_sort(mlist):
    if len(mlist) < 2: return mlist
    size = int(len(mlist)/2)
    return merge(merge_sort(mlist[:size]), merge_sort(mlist[size:]))

def merge(l, r):
    result = []
    i = j = 0
    # compares l and r lists and appends to temp list
    while i < len(l) and j < len(r):
        if l[i] < r[j]:
            result.append(l[i])
            i += 1
        else:
            result.append(r[j])
            j += 1  
    # adds remaining input to results to pass back
    result += l[i:]
    result += r[j:]
    return result

print msort('hellow world')
