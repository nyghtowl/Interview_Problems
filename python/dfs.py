'''
Depth First Search (DFS)

Input: tree of names and search for existance of one name
Output: true or false if the name is found

'''
class Node():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    #Recursive solution 
    def dfs(n, person):
        if not n:
            return False
        else:
            if n.val == person:
                return True
            else:
                if n.left:
                    return n.left.dfs(person)
                if n.right:
                    return n.right.dfs(person)


if __name__ == '__main__':


    #Build out the tree.
    n = Node('Lola')
    n2 = Node('Ann')
    n3 = Node('Rose')
    n4 = Node('Janice')
    n5 = Node('Harriet')
    n6 = Node('Louis')
    n7 = Node('Gertrude')

    n.left = n2
    n.right = n3
    n.right.left = n4
    n.right.right = n5
    n.left.left = n6
    n.left.right = n7

    #Test
    implementations = [n.dfs]

    person_search = 'Louis'
    person_search2 = 'George'
    
    result = True
    result2 = False

    for impl in implementations:
        print "trying %s" % impl
        print " f(%s) == %s: %s" % (person_search, person_search, impl(person_search) == result)
        print " f(%s) == %s: %s" % (person_search2, person_search2, impl(person_search2) == result2)
