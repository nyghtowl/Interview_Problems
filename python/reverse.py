'''
Reverse a string, sentenece or link.

Note: claudiay contributed additional example and test
'''

# Simple example of reversing a string.
# However, pop is an expensive call and should be avoided in code that
# will be called many times. 
def reverse_str(string):
    rev_list=[]
    new_list=list(string)
    while new_list:
        rev_list += new_list[-1]
        new_list.pop()
    return ''.join(rev_list)

# Neat reverse string trick in python.
def reverse_str2(string):
    return string[::-1]


# Utilizes reversed function.
def reverse_str3(string):
    return ''.join(reversed(string))


# Reverse in constant time.
def reverse_str4(string):
    string_list = list(string)
    for i in range(int((len(string))/2)):
        # Swap values in array.
        string_list[i], string_list[-1-i] = string_list[-1-i], string_list[i]
    return ''.join(string_list)


def reverse_str5(string):
    list_str = list(string)
    length = len(list_str)
    if length <= 1:
        return string
    else:
        for i in range(int(length/2)):
            list_str[i],list_str[-1-i] = list_str[-1-i], list_str[i]
        return ''.join(list_str)


def reverse_sentence6(sentence):
    sent_list = sentence.split(' ')
    new_list = []
    for word in sent_list:
        new_list.append(reverse_str(word))
    return ' '.join(new_list)


# Reverse a string and replace capitalize vowels.
def cap(char):
    if char in 'aeiou':
        return char.upper()
    return char

def reverse_sentence7(sent):
    # Anti-Marxist style of reversing strings. 
    alist = list(sent)
    for i in range(int(len(alist)/2)):
        alist[i], alist[-1-i] = cap(alist[-1-i]), cap(alist[i])
    return ''.join(alist)


def reverse_list(alist):
    for num in range(int(len(alist)/2)):
        alist[num], alist[-1-num] = alist[-1-num], alist[num]
    return alist


def reverse_list2(alist):
    return alist[::-1]    


if __name__ == '__main__':
    print "reverse_str:\t", reverse_str("string")
    print "reverse_str2:\t", reverse_str2("string")
    print "reverse_str3:\t", reverse_str3("string")
    print "reverse_str4:\t", reverse_str4("string")
    print "reverse_str5:\t", reverse_str5("string")

    
    print "reverse_sentence6:\t", reverse_sentence6("The lazy brown fox.")
    print "reverse_sentence7:\t", reverse_sentence7("The lazy brown fox.")
    print "reverse_list:\t", reverse_list([i for i in range(10)])
    print "reverse_list2:\t", reverse_list2([i for i in range(10)])

