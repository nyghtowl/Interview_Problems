''' 
Return the highest count of occurances of letters in a string or count of
numbers in an array/list 
'''
# if string is not sorted
def high_occ(string):
    letter_dict = {}
    high_value = 0
    for i in string:
        letter_dict[i] = letter_dict.get(i, 0) + 1
    for key, value in letter_dict.iteritems():
        if value > high_value:
            high_value = value
    return high_value

print 0, high_occ('hello world')

# print the count of the numbers in an array
def list_count(hal, n):
    count = 0
    if len(hal) <= 1 and hal[0] == n:
        count += 1      
    if n in hal and len(hal) > 1:
        pivot = int(len(hal)/2)
        if hal[pivot] == n:
            count += 1
            if hal[pivot+1] == n:
                count += 1
            if hal[pivot-1] == n:
                count += 1
        if hal[pivot] > n:
            count += list_count(hal[:pivot], n)
        if hal[pivot] < n:
            count += list_count(hal[pivot+1:], n)
    return count

print 1, list_count([2,4,5,5,5,6,7],7)

def list_count2(hal, n):
    return hal.count(n)

print 2, list_count2([2,4,5,5,5,6,7],5)

def list_count3(hal, n):
    return dict((n, hal.count(n)) for n in hal)

print 3, list_count3([2,4,5,5,5,6,7],5)

def list_count4(hal, n):
    count = 0
    if len(hal) <= 1 and hal[0] == n:
        return 1      
    if n in hal and len(hal) > 1:
        pivot = int(len(hal)/2)
        if hal[pivot] == n:
            if hal[pivot+1] == n:
                return (count + list_count(hal[:pivot], n))
            if hal[pivot-1] == n:                
                return (count + list_count(hal[pivot+1:], n))
        if hal[pivot] > n:
            return (count + list_count(hal[:pivot], n))
        if hal[pivot] < n:
            return (count + list_count(hal[pivot+1:], n))

print 4, list_count4([2,4,5,5,5,6,7],5)
