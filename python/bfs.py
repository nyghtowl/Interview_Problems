'''
Breadth First Search 

Input: tree and value to search for

Output: Breadth first search for a specified value in tree
'''


class Node():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def bfs(n, person):
        tree = []
        tree.append(n)
        ans = False
        while tree:
            n = tree.pop(0)
            if person == n.val:
                ans = True
            else:
                if n.left:
                    tree.append(n.left)
                if n.right:
                    tree.append(n.right)
        return ans


#Run, build & test the tree
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
    implementations = [n.bfs]

    person_search = 'Louis'
    person_search2 = 'George'

    result = True
    result2 = False

    for impl in implementations:
        print "trying %s" % impl
        print " f(%s) exists: %s" % (person_search, impl(person_search) == result)
        print " f(%s) does not exist: %s" % (person_search2, impl(person_search2) == result2)

