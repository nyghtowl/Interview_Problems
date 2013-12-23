'''
Double Linked List

In a doubly linked list, each element has the property that if element A has a "before" link to element B, then element B has an "after" link to element A

Provide a definition for an insert function that will create an ordered doubly linked list. This function is defined outside of the class Frob, and takes two arguments: a Frob that is currently part of a doubly linked list, and a new Frob. The new Frob will not initially have any "before" or "after" links to other Frobs. The function should mutate the list to place the new Frob in the correct location, with the resulting doubly linked list having appropriate "before" and "after" links.

Note that if a Frob is inserted with the same name as a pre-existing Frob, both names should be inserted in the final data structure (the exact ordering of the two identical Frobs does not matter)

From MIT CS 101 online class. 

'''

class Frob(object):
    def __init__(self, name):
        self.name = name
        self.before = None
        self.after = None
    def setBefore(self, before):
        self.before = before
    def setAfter(self, after):
        self.after = after
    def getBefore(self):
        return self.before
    def getAfter(self):
        return self.after
    def myName(self):
        return self.name
    def __repr__(self):
        return self.myName()

def insert(atMe, newFrob):
    """
    atMe: a Frob that is part of a doubly linked list
    newFrob:  a Frob with no links
    This procedure appropriately inserts newFrob into the linked list that atMe is a part of.
    """

    def set_frob(middle_frob, before_frob=None, after_frob=None):
        if before_frob:
            middle_frob.setBefore(before_frob)
            before_frob.setAfter(middle_frob)        
        if after_frob:
            after_frob.setBefore(middle_frob)
            middle_frob.setAfter(after_frob)

    def find_first():
        temp_frob = atMe
        while temp_frob.getAfter():
            temp_frob = temp_frob.getAfter()
            if temp_frob.myName() >= newFrob.myName():
                return temp_frob.getBefore()
        return temp_frob

    def find_last():
        temp_frob = atMe
        while temp_frob.getBefore():
            temp_frob = temp_frob.getBefore()
            if temp_frob.myName() <= newFrob.myName():
                return temp_frob.getAfter()
        return temp_frob

    if atMe.myName() == newFrob.myName():
        set_frob(newFrob, atMe.getBefore(), atMe)

    elif atMe.myName() < newFrob.myName():
        before_val = find_first()
        set_frob(newFrob, before_val, before_val.getAfter())

    elif atMe.myName() > newFrob.myName():
        after_val = find_last()
        set_frob(newFrob, after_val.getBefore(), after_val)

if __name__ == '__main__':
    #Test section

    eric = Frob('eric')
    andrew = Frob('andrew')
    ruth = Frob('ruth')
    fred = Frob('fred')
    martha = Frob('martha')

    insert(eric, andrew)
    insert(eric, ruth)
    insert(eric, fred)
    insert(ruth, martha)
    insert(eric, Frob('martha'))

    def find_front(start):
        if start.getBefore():
            return find_front(start.getBefore())
        else:
            return start

    def show_tree(node):
        temp = node
        while temp:
            print temp
            temp = temp.getAfter()

    # Show the linked list 
    front = find_front(eric)
    show_tree(front) # andrew eric fred martha martha ruth


