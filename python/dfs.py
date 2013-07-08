'''
Depth First Search
'''
class Node():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def dfs(n):
        hold = ''
        if not n:
            return
        else:
            hold = '%s ' % n.val
            if n.left:
                hold += '%s' % n.left.dfs()    
            if n.right:
                hold += '%s' % n.right.dfs()

        return hold

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
    
    result = 'Lola Ann Louis Gertrude Rose Janice Harriet '

    for impl in implementations:
        print "trying %s" % impl
        print " f(tree) == %s: %s" % (result, impl() == result)



