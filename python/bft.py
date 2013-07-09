'''
Breadth First Traversal

Input: tree
Output: printing out results of the tree by traversing the tree.
'''


class Node():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


    #Prints each value moving across each layer
    def bft(self):
        q = []
        ans = []
        q.append(self)
        while q:
            n = q.pop(0)
            ans.append(n.val)
            if n.left:
                q.append(n.left)
            if n.right:
                q.append(n.right)
        return ' '.join(ans)


    #Prints each level on a separate line.
    def bft2(self):
        q = []
        q2 = []
        ans = []
        q.append(self)
        while q:
            n = q.pop(0)
            ans.append(n.val)
            if n.left:
                q2.append(n.left)
            if n.right:
                q2.append(n.right)
            if len(q) == 0:
                q = q2
                q2 =[]
                ans.append('\n')
        return ' '.join(ans)


    #Variation that prints one line breadth.
    def bft3(self):
        parent = [self]
        ans = []
        while parent:
            children = []
            for i, node in enumerate(parent):
                ans.append(node.val)
                if node.left:
                    children.append(node.left)
                if node.right:
                    children.append(node.right) 
            parent = children
        return ' '.join(ans)



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
    implementations = [n.bft,n.bft3]
    implementations2 = [n.bft2]

    result1 = 'Lola Ann Rose Louis Gertrude Janice Harriet'
    result2 = 'Lola \n Ann Rose \n Louis Gertrude Janice Harriet \n'

    for impl in implementations:
        print "trying %s" % impl
        print " f(tree) == %s: %s" % (result1, impl() == result1)


    for impl in implementations2:
        print "trying %s" % impl
        print " f(tree) == %s: %s" % (result2, impl() == result2)
