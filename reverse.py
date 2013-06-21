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

print 0, rev_str('hello')

#---

def rev_str2(string):
    return string[::-1]

print 2, rev_str2('example')
    
#---

#utilize reversed function
def rev_str3(string):
    return ''.join(reversed(string))

#---

# reverse in constant time
def rev_str4(string):
    string_list = list(string)
    for i in range(int((len(string))/2)):
        string_list[i],string_list[-1-i] = string_list[-1-i],string_list[i]
    return ''.join(string_list)

print 4, rev_str4('nighttime')

#---

def rev_str5(string):
    list_str = list(string)
    length = len(list_str)
    if length <= 1:
        return string
    else:
        for i in range(int(length/2)):
            list_str[i],list_str[-1-i] = list_str[-1-i], list_str[i]
        return ''.join(list_str)

#---

def rev_sentence6(sentence):
    sent_list = sentence.split(' ')
    new_list = []
    for word in sent_list:
        new_list.append(rev_str(word))
    return ' '.join(new_list)


print 6, rev_sentence6('hello world')
#---

#reverse a string and replace capitalize vowels

def cap(char):
    if char in 'aeiou':
        return char.upper()
    return char

def rev_sentence7(sent):
    alist = list(sent)
    for i in range(int(len(alist)/2)):
        alist[i], alist[-1-i] = cap(alist[-1-i]), cap(alist[i])
    return ' '.join(alist)

print 7, rev_sentence7('hello world')

#---

def rev_list(alist):
    for num in range(int(len(alist)/2)):
        alist[num], alist[-1-num] = alist[-1-num], alist[num]
    return alist

print 0, rev_list(['h','e','l','l','o'])


#---

def rev_list2(alist):
    return alist[::-1]    

