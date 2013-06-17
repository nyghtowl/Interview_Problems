'''
reverse a string or link
'''

def rev_str(string):
    rev_list=[]
    new_list=list(string)
    while new_list:
        rev_list += new_list[-1]

        new_list.pop()
    return ''.join(rev_list)

print 1, rev_str('hello')

def rev_str2(string):
    return string[::-1]

def rev_list(list):
    return list[::-1]    
    
def rev_str3(string):
    return ''.join(reversed(string))

# reverse in constant time
def rev_str4(string):
    string_list = list(string)
    for i in range(int((len(string))/2)):
        string_list[i],string_list[-1-i] = string_list[-1-i],string_list[i]
    return ''.join(string_list)

print 1.4, rev_str4('nighttime')


def reverse_str(string):
    list_str = list(string)
    length = len(list_str)
    if length <= 1:
        return string
    else:
        for i in range(int(length/2)):
            list_str[i],list_str[-1-i] = list_str[-1-i], list_str[i]
        return ''.join(list_str)

def rev_sentence(sentence):
    sent_list = string.split(' ')
    new_list = []
    for word in sent_list:
        new_list.append(reverse_str(word))
    return ' '.join(new_list)


print 3, reverse_str('hello world')

def rev_str5(alist):
    for num in range(int(len(alist)/2)):
        alist[num], alist[-1-num] = alist[-1-num], alist[num]
    return alist

print 4, rev_str5(['h','e','l','l','o'])

def rev_str6(sub):
    return sub[::-1]

print 5, rev_str6('example')


