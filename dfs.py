'''
Depth First Search
'''

class Node_DFS():
    def __init__(self):
        self.val = val
        self.left = None
        self.right = None

    #Return nodes in order of depth
    def dfs(n):
        result = ''
        if not n:
            return
        else:
            result = '%r' % n.val
            if n.left:
                result += '%r' % dfs(n.left)    
            if n.right:
                result += '%r' % dfs(n.right)

        return result

#Build out the tree.
n = Node('Lola')
n2 = Node('Ann')
n3 = Node('Rose')
n.left = n2
n.right = n3
