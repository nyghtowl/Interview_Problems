'''
Depth First Search
'''
class Node_DFS():
    def __init__(self):
        self.val = val
        self.left = None
        self.right = None

    def dfs(n):
        hold = ''
        if not n:
            return
        else:
            hold = '%r' % n.val
            if n.left:
                hold += '%r' % dfs(n.left)    
            if n.right:
                hold += '%r' % dfs(n.right)

        return hold

n = Node('Lola')
n2 = Node('Ann')
n3 = Node('Rose')
n.left = n2
n.right = n3
