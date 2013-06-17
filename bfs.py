
# Breadth First Search
class Node():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def bft(self):
        q = []
        q.append(self)
        while q:
            n = q.pop(0)
            print n.val
            if n.left:
                q.append(n.left)
            if n.right:
                q.append(n.right)

    def bft2(self):
        q = []
        q2 = []
        q.append(self)
        while q:
            n = q.pop(0)
            print n.val,
            if n.left:
                q2.append(n.left)
            if n.right:
                q2.append(n.right)
            if len(q) == 0:
                q = q2
                q2 =[]
                print ""

    def bft3(self):
        parent = [self]
        while parent:
            children = []
            for i, node in enumerate(parent):
                print node.val,
                if node.left:
                    children.append(node.left)
                if node.right:
                    children.append(node.right) 
            parent = children
            print ""


n = Node('Lola')
n2 = Node('Ann')
n3 = Node('Rose')
n4 = Node('Janice')
n5 = Node('Harriet')
n6 = Node('Louis')
n.left = n2
n.right = n3
n.right.left = n4
n.right.right = n5
n.left.left = n6
n.bft3()