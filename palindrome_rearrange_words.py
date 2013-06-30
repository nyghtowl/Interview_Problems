'''
Palindrome Part 2 

Input: List of words
Output: Rearrange and print if can make a palindrome

'''


def pal(word):
    a_dict = {}
    for i,letter in enumerate(word):
        a_dict[letter] = a_dict.get(letter, 0) + 1
    if   
    print a_dict

def palindrome(words):
    for i, word in enumerate(words):
        print i, word
        counter = {}
        for j,letters in enumerate(word):
             counter[letters] = counter.get(letters, 0) + 1
        sides = []
        center = deque()
        for letter, occurrences in counter.items():
            repetitions, odd_count = divmod(occurrences, 2)
            if not odd_count:
                sides.append(letter * repetitions)
                continue
            if center:
                print "Value Error"
                center = deque()
                break
                # raise ValueError("no palindrome exists for '{}'".format(letters))
            center.append(letter * occurrences)
        center.extendleft(sides)
        center.extend(sides)
        if inner:
            print ''.join(center)
    return ' '.join(result)


class deque(object):
    '''
    deque data structure - can be imported from a library
    '''

    def __init__(self, iterable=(), maxsize=-1):
        if not hasattr(self, 'data'):
            self.left = self.right = 0
            self.data = {}
        self.maxsize = maxsize
        self.extend(iterable)

    def append(self, x):
        self.data[self.right] = x
        self.right += 1
        if self.maxsize != -1 and len(self) > self.maxsize:
            self.popleft()
        
    def appendleft(self, x):
        self.left -= 1        
        self.data[self.left] = x
        if self.maxsize != -1 and len(self) > self.maxsize:
            self.pop()      
        
    def pop(self):
        if self.left == self.right:
            raise IndexError('cannot pop from empty deque')
        self.right -= 1
        elem = self.data[self.right]
        del self.data[self.right]         
        return elem
    
    def popleft(self):
        if self.left == self.right:
            raise IndexError('cannot pop from empty deque')
        elem = self.data[self.left]
        del self.data[self.left]
        self.left += 1
        return elem

    def clear(self):
        self.data.clear()
        self.left = self.right = 0

    def extend(self, iterable):
        for elem in iterable:
            self.append(elem)

    def extendleft(self, iterable):
        for elem in iterable:
            self.appendleft(elem)

    def rotate(self, n=1):
        if self:
            n %= len(self)
            for i in xrange(n):
                self.appendleft(self.pop())

    def __getitem__(self, i):
        if i < 0:
            i += len(self)
        try:
            return self.data[i + self.left]
        except KeyError:
            raise IndexError

    def __setitem__(self, i, value):
        if i < 0:
            i += len(self)        
        try:
            self.data[i + self.left] = value
        except KeyError:
            raise IndexError

    def __delitem__(self, i):
        size = len(self)
        if not (-size <= i < size):
            raise IndexError
        data = self.data
        if i < 0:
            i += size
        for j in xrange(self.left+i, self.right-1):
            data[j] = data[j+1]
        self.pop()
    
    def __len__(self):
        return self.right - self.left

    def __cmp__(self, other):
        if type(self) != type(other):
            return cmp(type(self), type(other))
        return cmp(list(self), list(other))
            
    def __repr__(self, _track=[]):
        if id(self) in _track:
            return '...'
        _track.append(id(self))
        r = 'deque(%r)' % (list(self),)
        _track.remove(id(self))
        return r
    
    def __getstate__(self):
        return (tuple(self),)
    
    def __setstate__(self, s):
        self.__init__(s[0])
        
    def __hash__(self):
        raise TypeError
    
    def __copy__(self):
        return self.__class__(self)
    
    def __deepcopy__(self, memo={}):
        from copy import deepcopy
        result = self.__class__()
        memo[id(self)] = result
        result.__init__(deepcopy(tuple(self), memo))
        return result


def compute_palindromes(words_list):
    for i, word in enumerate(words_list):
        count_dict = {}
        for j, letter in enumerate(word):
            if letter in count_dict:
                count_dict[letter] += 1
            else:
                count_dict[letter] = 1
        print count_dict

        odd_count = 0
        for key, value in count_dict.iteritems():
            if value % 2 != 0:
                odd_count +=1
        if odd_count > 1:
            print -1
            return

        start = []
        end = []
        middle = None   
    
        for key, value in count_dict.iteritems():
            if value % 2 == 0:
                val = int(value)/2
                start.append(key * val)
                end.append(key * val)
            else:
                middle = key
    
        if middle:
            start.append(middle)
        end.reverse()
        start.extend(end)
        string = "".join(start)
        print string


pal('hello')
palindrome(['talliat', 'eded', 'memo'])
words = ["cecarar", "nono", "abbbbb"]
